args = parser.parse_args()
if args.command == "download":
    downloader = Downloader(args.output_dir)
    downloader.download_all_wiktionaries()
elif args.command == "dataset":
    create_csv_dataset_from_dump(args.dumps_folder_path)
