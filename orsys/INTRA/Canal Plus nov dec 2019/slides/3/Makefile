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

unsupervised := \
    unsupervised.pdf \
    dimensionality-reduction.pdf \
    pca-lda.pdf \
    pca-variantes.pdf \
    unsupervised-metrics.pdf \
    hierarchical-clustering.pdf \
    algorithme-em.pdf \
    kmeans-gaussian.pdf \
    pca-classification-hierarchique-composantes-principales.pdf \

tp1 :=\
    tp-unsupervised.pdf

recommandation := \
    recommander-system.pdf \
    filtrage-colaboratif.pdf \
    filtrage-colaboratif-user-based.pdf \
    filtrage-colaboratif-item-based.pdf \
    filtrage-colaboratif-eval.pdf \
    filtrage-colaboratif-extend.pdf \
    filtrage-colaboratif-conclusion.pdf \

series := \
    sequential-data.pdf \
    sequential-first-approach.pdf \
    series-arma.pdf \
    series-arima.pdf \
    series-sarima.pdf \
    series-varmax.pdf \
    sequential-models.pdf \
    markov-model.pdf \
    hmm-latest.pdf \

craftmoncul := \
    ml-craftmoncul.pdf \

tp2 :=\
    tp-arma.pdf

title = title.pdf

questions = questions.pdf

slides.pdf: $(title) $(supervised) $(unsupervised) $(tp1) $(recommandation) $(series) $(craftmoncul) $(tp2)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
