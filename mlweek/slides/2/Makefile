intro := \
    0-about.pdf \
    0-rappels.pdf \

cours1 := \
    1-regression-lineaire.pdf \
    1-cost-error-function.pdf \
    1-optimisation.pdf \
    1-derivation-gradient.pdf \

tp1 := \
    2-regression-lineaire-tp.pdf \

cours2 := \
    3-regression-logistique.pdf \
    3-NN.pdf \

tp2 := \
    4-regression-logistique-tp.pdf \


title = title.pdf 

questions = questions.pdf 


cours.pdf: $(title)  $(intro) $(cours1) $(tp1) $(cours2) $(tp2)
	pdftk $+ cat output $@

intro.pdf: $(title) $(intro)
	pdftk $+ cat output $@

tp.pdf: $(tp)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
