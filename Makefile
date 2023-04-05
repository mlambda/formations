dirs := figures/plots

install:
	mkdir -p "$(HOME)/texmf/tex/latex/formation"
	for f in "$(PWD)/stys/"* ; do \
		ln -fs "$$f" "$(HOME)/texmf/tex/latex/formation/$$(basename "$$f")" ; \
	done

check:
	black --check $(dirs)
	isort --check-only $(dirs)
	mypy $(dirs)
	flake8 --count $(dirs)

.PHONY: install check
