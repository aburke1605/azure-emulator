import argparse
import subprocess
import yaml


def new(_):
    yaml.safe_dump(
        {"services": {}, "volumes": {}},
        open("compose.yml", "w")
    )


def init(args):
    config = yaml.safe_load(open("compose.yml", "r"))
    if "database" in args.services:
        config["services"]["database"] = yaml.safe_load(open("templates/database.yml", "r"))
    yaml.safe_dump(config, open("compose.yml", "w"))


def up(_):
    result = subprocess.run(["docker", "compose", "up", "--detach"])


def down(_):
    result = subprocess.run(["docker", "compose", "down"])


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(
    dest="command",
    required=True
)


def add_subparser(name: str, func, *args, **kwargs):
    p = subparsers.add_parser(name, **kwargs)
    p.set_defaults(func=func)
    return p


add_subparser("new", new,
    help="create a new blank stack")

add_subparser("init", init,
    help="add default service(s) to the stack")\
.add_argument(
    "services",
    type=str,
    nargs="+",
    choices=[
        "webapp",
        "database",
    ],
    help="list of service names to add"
)

add_subparser("up", up,
    help="emulate deployment")

add_subparser("down", down,
    help="destroy emulator")

args = parser.parse_args()
args.func(args)
