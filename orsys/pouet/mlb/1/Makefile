title = title.pdf

intro := \
    about.pdf \

python-jupyter := \
    python-intro.pdf \
    notebook-intro.pdf \
    notebook-jupyter-install.pdf \

modelisation := \
    ml-intro.pdf \
    ml-data-preparation.pdf \
    ml-learn.pdf \

tp1 := \
    tp-data-analysis.pdf \

questions = questions.pdf

debug := \
    about.pdf \

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(python-jupyter) $(modelisation) $(questions) $(tp1) 
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
