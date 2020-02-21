title = title.pdf

unsupervised := \
    unsupervised.pdf \
    dimensionality-reduction.pdf \
    pca-lda.pdf \
    algorithme-em.pdf \
    kmeans-gaussian.pdf \
    anomaly-detection-light.pdf \

supervised := \
    naive-bayes.pdf \
    trees.pdf \
    random-forest.pdf \
    regression-lineaire.pdf \
    cost-error-function.pdf \
    optimisation.pdf \
    derivation-gradient.pdf \
    regression-logistique.pdf \
    nn-intro.pdf \
    svm.pdf \

tp1 := \
    tp-unsupervised.pdf \

tp2 := \
    tp-supervised.pdf \

questions = questions.pdf

slides.pdf: $(title) $(unsupervised) $(tp1) $(questions) $(supervised) $(tp2)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
