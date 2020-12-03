install:
	mkdir -p "$(HOME)/texmf/tex/latex/formation"
	ln -fs "$(PWD)/formation.sty" "$(HOME)/texmf/tex/latex/formation/formation.sty"

.PHONY: install
