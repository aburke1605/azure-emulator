import argparse
import yaml

parser = argparse.ArgumentParser()
parser.add_argument(
    "--new",
    action='store_true',
    help="create a new blank stack"
)
parser.add_argument(
    "--init",
    type=str,
    nargs="+",
    choices=[
        "webapp",
        "database",
    ],
    help="add service(s) to the stack"
)
args = parser.parse_args()

if args.new:
    yaml.dump(
        {"services": {}, "volumes": {}},
        open("compose.yml", "w")
    )

if args.init:
    if "database" in args.init:
        pass
