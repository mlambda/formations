intro := \
    0-about.pdf

cours := \
    1-machine-learning.pdf \
    1-probabilities.pdf \
    1-statistics.pdf \
    1-algebre.pdf \
    questions.pdf \
    1-data.pdf \
    1-features-and-modeling.pdf \
    1-teaser.pdf 

tp := \
    2-python-plot-data.pdf \
    questions.pdf

title = title.pdf

questions = questions.pdf

questions = template.pdf

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

clean-tex: clean
	a=$(ls *tex);b=$(grep "[^*%]\.pdf" Makefile | sed "s/[ \][ \]*$//g;s/^.*  *//g" | grep -v "(" | sed "s/\.pdf/.tex/g" | sort | uniq);rm $(echo -e "$a\n$b" | sort | uniq -ic | sort -n | grep -v " 2 " | sed "s/^.* //g")

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
