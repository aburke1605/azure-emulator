import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--new",
    action='store_true',
    help="create a new blank stack"
)
args = parser.parse_args()

print(args.new)

