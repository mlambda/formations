from pathlib import Path
from re import compile as re_compile
from sys import argv

from deckz.paths import GlobalPaths


paths = GlobalPaths.from_defaults(Path.cwd())

image = argv[1]
pattern = re_compile(fr'(\\V{{\[?"{image}".*\]? \| image}})')
for f in paths.shared_latex_dir.rglob("*.tex"):
    if pattern.search(f.read_text(encoding="utf8")):
        print(str(f))

