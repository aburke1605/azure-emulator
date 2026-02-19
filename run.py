import argparse
import subprocess
import yaml

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

parser_new = subparsers.add_parser(
    "new",
    help="create a new blank stack"
)

parser_init = subparsers.add_parser(
    "init",
    help="add default service(s) to the stack"
)
parser_init.add_argument(
    "services",
    type=str,
    nargs="+",
    choices=[
        "webapp",
        "database",
    ],
    help="list of service names to add"
)

parser_up = subparsers.add_parser(
    "up",
    help="emulate deployment"
)

parser_down = subparsers.add_parser(
    "down",
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
