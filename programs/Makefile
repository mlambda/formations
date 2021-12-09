markdowns := $(wildcard *.md)
pdfs := $(markdowns:%.md=pdfs/%.pdf)

all: $(pdfs)

pdfs/%.pdf: %.md
	mkdir -p pdfs
	pandoc $< \
		--pdf-engine=xelatex \
		--variable='fontfamily:libertine' \
		--output $@

.PHONY: all
