supervised := \
    naive-bayes.pdf \
    trees.pdf \
    random-forest.pdf \
    regression-lineaire.pdf \
    cost-error-function.pdf \
    optimisation.pdf \
    derivation-gradient.pdf \
    regression-polynomiale.pdf \
    regression-logistique.pdf \
    nn-intro.pdf \
    svm.pdf \

title = title.pdf

tp = tp.pdf

questions = questions.pdf

slides.pdf: $(title) $(supervised) $(questions) $(tp)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
