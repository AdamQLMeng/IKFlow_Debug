import argparse


from ikflow_local import visualizations
from ikflow_local.utils import set_seed
from ikflow_local.model_loading import get_ik_solver

set_seed()

_VALID_DEMO_NAMES = ["oscillate_target", "oscillate_latent"]
VIS_FN_ARGUMENTS = {"oscillate_target": {"nb_sols": 10, "fixed_latent": True}, "oscillate_latent": {}}

""" Example usage. Note that `model_name` should match an entry in `model_descriptions.yaml`

# Panda
python scripts/visualize.py --model_name=panda__full__lp191_5.25m --demo_name=oscillate_latent
python scripts/visualize.py --model_name=panda__full__lp191_5.25m --demo_name=oscillate_target

# Rizon4
python scripts/visualize.py --model_name rizon4__snowy-brook-208__global_step=2.75M --demo_name=oscillate_latent
python scripts/visualize.py --model_name rizon4__snowy-brook-208__global_step=2.75M --demo_name=oscillate_target

# Fetch
python scripts/visualize.py --model_name=fetch__large__ns183_9.75m --demo_name=oscillate_latent
python scripts/visualize.py --model_name=fetch__large__ns183_9.75m --demo_name=oscillate_target

python scripts/visualize.py --model_name=fetch__large__ns183_9.75m --demo_name=oscillate_latent
python scripts/visualize.py --model_name=fetch__large__ns183_9.75m --demo_name=oscillate_target
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="evaluate.py - evaluates IK models")
    parser.add_argument("--model_name", type=str, help="Name of the saved model to look for in model_descriptions.yaml")
    parser.add_argument("--visualization_program", type=str, help="One of [---TODO---]")
    parser.add_argument("--demo_name", type=str, help="One of ['oscillate_latent', 'oscillate_target']")
    args = parser.parse_args()

    assert args.demo_name in _VALID_DEMO_NAMES, f"Invalid demo name. Must be one of {_VALID_DEMO_NAMES}"

    # Build IKFlowSolver and set weights
    ik_solver, hyper_parameters = get_ik_solver(args.model_name)

    fn = getattr(visualizations, args.demo_name)
    fn(ik_solver, **VIS_FN_ARGUMENTS[args.demo_name])
