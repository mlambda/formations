intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-ml-craftmanship.pdf \
    1-my-firsts-models.pdf \
    1-svm.pdf \
    1-random-forest.pdf \

tp := \
    2-random-forest-tp.pdf \
    2-svm-tp.pdf \

title = title.pdf 

questions = questions.pdf 


cours.pdf: $(title)  $(intro) $(cours)
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
