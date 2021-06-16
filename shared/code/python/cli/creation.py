import argparse

parser = argparse.ArgumentParser(description="Create datasets.")
parser.add_argument("output_dir", help="Path to the directory.")
parser.add_argument("--langs", nargs="+", help="Langs to consider.")
parser.add_argument("--max-size", type=int, help="Maximum size in ko.")
