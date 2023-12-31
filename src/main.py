import sys
sys.path.append("../src/")
import argparse
import numpy as np
from utils import flatten_dict

import wandb
import os
from hydra import (
    initialize, initialize_config_module, 
    initialize_config_dir, compose,
)
from hydra.utils import instantiate
from omegaconf import OmegaConf


if not OmegaConf.has_resolver("eval"):
    def resolver(x):
        import numpy as np
        return eval(x)
    OmegaConf.register_new_resolver("eval", resolver)


def simulate_rounds(model, rewards, actions_hist, X_global, y_global, batch_st, batch_end):
    np.random.seed(batch_st)
    actions_this_batch = model.predict(X_global[batch_st:batch_end, :]).astype('uint8')
    rewards.append(y_global[np.arange(batch_st, batch_end), actions_this_batch].sum())
    new_actions_hist = np.append(actions_hist, actions_this_batch)
    np.random.seed(batch_st)
    model.fit(
        X_global[:batch_end, :], 
        new_actions_hist, 
        y_global[np.arange(batch_end), new_actions_hist],
    )
    wandb.log(
        {
            "reward": y_global[np.arange(batch_st, batch_end), actions_this_batch].sum(),
            "regret": (
                y_global[np.arange(batch_st, batch_end),:].max(axis=1) 
                - 
                y_global[np.arange(batch_st, batch_end), actions_this_batch].flatten()
            ).sum(),
            "reward_avg": y_global[np.arange(batch_end), new_actions_hist].sum()/(batch_end/(batch_end-batch_st))
        }
    )
    return new_actions_hist


def run_model(model, X,y, cfg):
    batch_size = cfg.batch_size
    nchoices = y.shape[1]
    rewards = []
    first_batch = X[:batch_size, :]
    np.random.seed(cfg.seed)
    action_chosen = np.random.randint(nchoices, size=batch_size)
    rewards_received = y[np.arange(batch_size), action_chosen]
    actions = action_chosen.copy()
    model.fit(X=first_batch, a=action_chosen, r=rewards_received)
    for i in range(int(np.floor(X.shape[0] / batch_size))):
        batch_st = (i + 1) * batch_size
        batch_end = (i + 2) * batch_size
        batch_end = np.min([batch_end, X.shape[0]])
        if batch_end<=batch_st:
            continue
        actions = simulate_rounds(
            model,
            rewards,
            actions,
            X, 
            y,
            batch_st, 
            batch_end
        )
        wandb.log({"epoch": i})
        if cfg.debug and 3 < i: 
            break
    return rewards


def run_experiment(name):
    with initialize(
        version_base=None, 
        config_path="../conf/", 
    ):
        cfg = compose(
            config_name="config.yaml",
            # return_hydra_config=True, 
            overrides=[f"+experiment={name}"]
        )
    model = instantiate(cfg.model)
    parser = instantiate(cfg.parser)
    X,y = parser()
    flat_dict = flatten_dict(OmegaConf.to_container(cfg))
    run = wandb.init(project=cfg.project, config=flat_dict)
    reward = run_model(model, X,y, cfg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e','--experiment', dest="experimets", nargs='+', help='<Required> Set flag', required=True)
    args = parser.parse_args()
    for i in args.experiments:
		name = f"mediamill_{str(i).zfill(3)}"
		run_experiment(name)
