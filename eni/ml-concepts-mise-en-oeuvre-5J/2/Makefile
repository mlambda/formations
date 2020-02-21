modules-d1 := \
    1-regression-lineaire.pdf \
    1-cost-error-function.pdf \
    1-optimisation.pdf \
    1-derivation-gradient.pdf \
    1-regression-logistique.pdf \
    1-svm.pdf \
    1-trees.pdf \

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
