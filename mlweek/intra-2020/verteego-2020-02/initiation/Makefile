title = title.pdf

intro := \
    about.pdf \

python-jupyter := \
    python-intro.pdf \
    notebook-intro.pdf \

modelisation := \
    ml-intro.pdf \
    ml-data-preparation.pdf \
    ml-learn-supervised.pdf \

bda-tp1 := \
    bda-tp1.pdf \

title-supervised = title-supervised.pdf

supervised := \
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

title-series = title-series.pdf

series := \
    sequential-data.pdf \
    sequential-first-approach.pdf \
    sequential-models.pdf \
    markov-model.pdf \
    hmm-latest.pdf \

tp-reglin := \
    tp-reglin.pdf \

tp-hmm := \
    tp-hmm.pdf \

evaluation := \
    evaluation-initiation.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(python-jupyter) $(modelisation) $(questions) $(bda-tp1) $(title-supervised) $(supervised) $(questions) $(tp-reglin) $(title-series) $(series) $(questions) $(evaluation)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

tex:
	./make-tex.sh

clean-tex:
	./clean-tex.sh

.PHONY: clean
