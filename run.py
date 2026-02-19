import argparse
import subprocess
import yaml


def new(args):
    yaml.safe_dump(
        {"services": {}, "volumes": {}},
        open("compose.yml", "w")
    )


def init(args):
    config = yaml.safe_load(open("compose.yml", "r"))
    if "database" in args.services:
        config["services"]["database"] = yaml.safe_load(open("templates/database.yml", "r"))
    yaml.safe_dump(config, open("compose.yml", "w"))


def up(args):
    result = subprocess.run(["docker", "compose", "up", "--detach"])


def down(args):
    result = subprocess.run(["docker", "compose", "down"])


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

subparsers.add_parser(
    "new",
    help="create a new blank stack"
).set_defaults(func=new)

subparsers.add_parser(
    "init",
    help="add default service(s) to the stack"
).add_argument(
    "services",
    type=str,
    nargs="+",
    choices=[
        "webapp",
        "database",
    ],
    help="list of service names to add"
).set_defaults(func=init)

subparsers.add_parser(
    "up",
    help="emulate deployment"
).set_defaults(func=up)

subparsers.add_parser(
    "down",
    help="destroy emulator"
).set_defaults(func=down)

args = parser.parse_args()
args.func(args)
