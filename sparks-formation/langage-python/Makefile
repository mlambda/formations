notebook := Langage\ Python.ipynb
template := slides.tex.j2

all: $(notebook) $(template)
	jupyter nbconvert $(notebook) --execute --to pdf --template-file $(template)

.PHONY: all
