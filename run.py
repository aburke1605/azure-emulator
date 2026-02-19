import argparse
import subprocess
import yaml

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

subparsers.add_parser(
    "new",
    help="create a new blank stack"
)

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
)

subparsers.add_parser(
    "up",
    help="emulate deployment"
)

subparsers.add_parser(
    "down",
    help="destroy emulator"
)

args = parser.parse_args()


def new():
    yaml.safe_dump(
        {"services": {}, "volumes": {}},
        open("compose.yml", "w")
    )


def init():
    config = yaml.safe_load(open("compose.yml", "r"))
    if "database" in args.services:
        config["services"]["database"] = yaml.safe_load(open("templates/database.yml", "r"))
    yaml.safe_dump(config, open("compose.yml", "w"))


def up():
    result = subprocess.run(["docker", "compose", "up", "--detach"])


def down():
    result = subprocess.run(["docker", "compose", "down"])


switcher = {
    "new": new,
    "init": init,
    "up": up,
    "down": down
}
switcher.get(args.command, lambda: None)()
