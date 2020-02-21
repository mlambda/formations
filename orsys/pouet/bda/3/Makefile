unsupervised := \
    unsupervised.pdf \
    dimensionality-reduction.pdf \
    pca-lda.pdf \
    pca-variantes.pdf \
    unsupervised-metrics.pdf \
    hierarchical-clustering.pdf \
    algorithme-em.pdf \
    kmeans-gaussian.pdf \
    dbscan.pdf \
    clustering-conclusions.pdf \
    pca-classification-hierarchique-composantes-principales.pdf \
    pca-inverse.pdf \
    anomaly-detection.pdf \

title = title.pdf

tp_unsupervised = tp.pdf

questions = questions.pdf

slides.pdf: $(title) $(unsupervised) $(tp_unsupervised)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
