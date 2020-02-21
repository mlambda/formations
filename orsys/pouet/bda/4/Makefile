title = title.pdf

text-mining := \
    text-intro.pdf \
    text-pretraitements.pdf \
    text-vectors.pdf \

craftmanship := \
    ml-craftmoncul.pdf \

problematiques := \
    problematiques.pdf \
    problematiques-juridique.pdf \


text-tp := \
    text-tp.pdf \

questions = questions.pdf

debug.pdf: $(title) $(pouet)
	pdftk $+ cat output $@

slides.pdf: $(title) $(text-mining) $(craftmanship) $(problematiques) $(questions) $(text-tp)
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
