import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    type=str,
    required=True
)
args = parser.parse_args()

print(args.test)

