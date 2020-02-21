modules-d1 := \
    1-dimensionality-reduction.pdf \
    1-pca-lda.pdf \
    1-unsupervised.pdf \
    1-algorithme-em.pdf \
    1-kmeans-gaussian.pdf \
    1-dbscan.pdf \
    1-unsupervised-metrics.pdf \
    1-clustering-conclusions.pdf \
    1-anomaly-detection.pdf \

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
