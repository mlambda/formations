all := \
    dataset-intro.pdf \
    ia-intro.pdf \
    ia-methodologie.pdf \
    ia-prerequis.pdf \
    ml-applications.pdf \
    ml-intro.pdf \
    nn-cnn.pdf \
    nn-gan.pdf \
    nn-intro.pdf \
    nn-learn.pdf \
    nn-reinforce.pdf \
    nn-rnn.pdf \
    tools-datasets.pdf \
    tools-deep.pdf \
    tools-ml.pdf \

all.pdf: $(all)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
