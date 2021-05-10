install:
	mkdir -p "$(HOME)/texmf/tex/latex/formation"
	for f in "$(PWD)/stys/"* ; do \
		ln -fs "$$f" "$(HOME)/texmf/tex/latex/formation/$$(basename "$$f")" ; \
	done

.PHONY: install
