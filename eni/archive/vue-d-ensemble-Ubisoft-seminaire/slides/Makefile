title = title.pdf

intro := \
    0-about.pdf \
    0-preambule.pdf \

ml-fast-review := \
    1-machine-learning.pdf \
    1-problematiques.pdf \

perspectives_globales := \
    4-tendencies-and-new-sectors.pdf \
    4-transport.pdf \
    4-sante.pdf \

pause = pause.pdf

perspectives_ubisoft := \
    1-RL.pdf \
    1-AlphaGo.pdf \
    1-videogame.pdf \
    1-misc.pdf \

questions = questions.pdf


debug.pdf: $(title) $(ml-fast-review)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(ml-fast-review) $(perspectives_globales) $(pause) $(perspectives_ubisoft) $(questions)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
