import argparse
import subprocess
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
parser.add_argument(
    "--up",
    action='store_true',
    help="emulate deployment"
)
parser.add_argument(
    "--down",
    action='store_true',
    help="destroy emulator"
)
args = parser.parse_args()

if args.new:
    yaml.safe_dump(
        {"services": {}, "volumes": {}},
        open("compose.yml", "w")
    )

if args.init:
    config = yaml.safe_load(open("compose.yml", "r"))
    if "database" in args.init:
        config["services"]["database"] = yaml.safe_load(open("templates/database.yml", "r"))
    yaml.safe_dump(config, open("compose.yml", "w"))

if args.up:
    result = subprocess.run(["docker", "compose", "up", "--detach"])

if args.down:
    result = subprocess.run(["docker", "compose", "down"])
