title = title.pdf

intro := \
    about.pdf \
    tf-intro.pdf \

nn-intro := \
    nn-intro.pdf \
    nn-learn.pdf \

nn-deep := \
    nn-problematiques.pdf \
    nn-optimize.pdf \
    nn-deep-optimize.pdf \
    nn-regularisation.pdf \

nn-tp := \
    dpl-tp1.pdf \

debug := \
    tf-intro.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(nn-intro) $(nn-deep) $(questions) $(nn-tp)
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
