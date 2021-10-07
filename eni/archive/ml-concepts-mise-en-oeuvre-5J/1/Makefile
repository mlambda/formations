modules-d1 := \
    0-about.pdf \
    1-introduction.pdf \
    2-maths.pdf \
    3-fundamentals.pdf \

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
