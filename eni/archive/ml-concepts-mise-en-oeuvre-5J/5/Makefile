modules-d1 := \
    1-ml-craftmanship.pdf \
    1-recommander-system.pdf \
    1-filtrage-colaboratif.pdf \
    1-filtrage-colaboratif-user-based.pdf \
    1-filtrage-colaboratif-item-based.pdf \
    1-filtrage-colaboratif-eval.pdf \
    1-filtrage-colaboratif-extend.pdf \
    1-filtrage-colaboratif-conclusion.pdf \


title = title.pdf

tp = tp.pdf

questions = questions.pdf

slides.pdf: $(title) $(modules-d1) $(tp)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
