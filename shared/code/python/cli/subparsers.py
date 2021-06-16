import argparse

parser = argparse.ArgumentParser(description="Create datasets.")
subparsers = parser.add_subparsers(help="Commands", dest="command")

download_parser = subparsers.add_parser("download")
download_parser.add_argument("output_dir")

dataset_parser = subparsers.add_parser("dataset")
dataset_parser.add_argument("dumps_folder_path")
