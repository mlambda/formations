import pathlib


home = pathlib.Path.home()
formations_dir = home / "work" / "formations"
print(formations_dir)
config_file = formations_dir / "config.yml"
print(config_file.with_suffix(".txt"))
print(config_file.name)
for item in formations_dir.iterdir():
    print(item)
