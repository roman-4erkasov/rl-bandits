
def flatten_dict(dd, separator ='.', prefix =''):
    return { 
        prefix + separator + k if prefix else k : v
        for kk, vv in dd.items()
        for k, v in flatten_dict(vv, separator, kk).items()
    } if isinstance(dd, dict) else { prefix : dd }


def get_mean_reward(reward_lst, batch_size=50):
    mean_rew=list()
    for r in range(len(reward_lst)):
        mean_rew.append(sum(reward_lst[:r+1]) * 1.0 / ((r+1)*batch_size))
    return mean_rew


