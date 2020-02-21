title = title.pdf

intro := \
    about.pdf \

data := \
    ml-data-intro.pdf \
    ml-data-sequential.pdf \
    ml-data-sources.pdf \
    ml-data-preparation.pdf \

ml := \
    ml-intro.pdf \

historique := \
    historique-ia.pdf \

ml-learn := \
    ml-learn.pdf \

unsupervised := \
    unsupervised.pdf \
    hierarchical-clustering.pdf \
    algorithme-em.pdf \
    dbscan.pdf \
    clustering-conclusions.pdf \
    anomaly-detection.pdf \
    dimensionality-reduction.pdf \
    pca-lda.pdf \
    pca-variantes.pdf \

supervised := \
    naive-bayes.pdf \
    regression-lineaire.pdf \
    cost-error-function.pdf \
    optimisation.pdf \
    derivation-gradient.pdf \
    regression-logistique.pdf \
    svm.pdf \
    gradient-boosted-tree.pdf \
    trees.pdf \
    random-forest.pdf \
    sequential-models.pdf \
    markov-model.pdf \
    hmm-latest.pdf \

neuralnet := \
    nn-intro.pdf \
    nn-cnn.pdf \
    rnn.pdf \
    rnn-variants.pdf \
    petit-jeu.pdf \
    gan.pdf \

reinforcement := \
    renforcement.pdf \
    rl-deep.pdf \
    alphago.pdf \

text := \
    text-intro.pdf \
    text-pretraitements.pdf \
    text-vectors.pdf \

actors := \
    gafa.pdf \
    chine.pdf \

tools := \
    hadoop-intro.pdf \
    spark-intro.pdf \
    r-scripts.pdf \
    python-intro.pdf \
    sklearn.pdf \
    keras-intro-short.pdf \

craftmanship := \
    ml-craftmoncul.pdf \

problematiques := \
    problematiques.pdf \
    problematiques-juridique.pdf \

domaines := \
    tendencies-and-new-sectors.pdf \
    transport.pdf \
    sante.pdf \
    coding.pdf

questions = questions.pdf


slides.pdf: $(title) $(intro) $(data) $(ml) $(historique) $(ml-learn) $(unsupervised) $(supervised) $(neuralnet) $(reinforcement) $(text) $(actors) $(tools) $(craftmanship) $(problematiques) $(domaines) $(questions)
	pdftk $+ cat output $@

actors.pdf: $(title) $(actors)
	pdftk $+ cat output $@

debug.pdf: $(title) $(data)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
