args = parser.parse_args()
command = args.command
delattr(args, "command")
if command == "download":
    downloader = Downloader(**vars(args))
    downloader.download_all_wiktionaries()
elif command == "dataset":
    create_csv_dataset_from_dump(**vars(args))