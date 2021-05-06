from pathlib import Path
from re import compile as re_compile
from sys import argv


image = argv[1]
pattern = re_compile(fr'(\\V{{\[?"{image}".*\]? \| image}})')
shared_latex_dir = Path("/home/fmg/FORMATIONS/slides/shared/latex")
for f in shared_latex_dir.rglob("*.tex"):
    if pattern.search(f.read_text(encoding="utf8")):
        print(str(f))