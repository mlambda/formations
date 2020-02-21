title = title.pdf

actors := \
    gafa.pdf \

tools := \
    hadoop-intro.pdf \
    spark-intro.pdf \
    kaggle.pdf \
    arXiv.pdf \
    github.pdf \
    cloud-computing.pdf \

craftmanship := \
    ml-craftmoncul.pdf \

problematiques := \
    problematiques.pdf \
    problematiques-juridique.pdf \

domaines := \
    tendencies-and-new-sectors.pdf \
    sante.pdf \
    coding.pdf \

demo1 := \
    demo-spark-tf-keras-cnn.pdf \

questions = questions.pdf

slides.pdf: $(title) $(actors) $(tools) $(craftmanship) $(problematiques) $(domaines) $(questions) $(demo1)
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
