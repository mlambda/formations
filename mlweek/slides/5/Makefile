intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-unsupervised.pdf \
    1-algorithme-em.pdf \
    1-kmeans-gaussian.pdf \
    1-dbscan.pdf \
    1-unsupervised-neural-network.pdf \
    1-unsupervised-metrics.pdf \
    1-clustering-conclusions.pdf \
    1-anomaly-detection.pdf \
    1-tp.pdf


title = title.pdf 

questions = questions.pdf 


cours.pdf: $(title)  $(intro) $(cours)
	pdftk $+ cat output $@

intro.pdf: $(title) $(intro)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean

tex:
	/bin/bash ../maketex.sh

clean-wipe-all-garbage: clean-pdfs
	/bin/bash ../clean-tex.sh
	cours.pdf
	clean
