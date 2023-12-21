
.PHONY:*

install:
	/usr/bin/python3.8 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt
	git clone https://github.com/vwxyzjn/cleanrl.git
	ve_cleanrl/bin/pip install -U pip
	ve_cleanrl/bin/pip install -r cleanrl/requirements/requirements.txt
	pip install wandb 
	pip install Cython
	pip install contextualbandits
	pip install -U scikit-learn
	pip install hydra-core --upgrade

