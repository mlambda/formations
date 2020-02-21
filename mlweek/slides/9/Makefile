intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-RL.pdf \
    1-RL-deep.pdf \
    1-dqn.pdf \
    1-AlphaGo.pdf \
    1-tp.pdf \

title = title.pdf 

questions = questions.pdf

cours.pdf: $(title)  $(intro) $(cours) $(questions) $(tp)
	pdftk $+ cat output $@

intro.pdf: $(title) $(intro)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean

tex:
	/bin/bash ../maketex.sh

clean-wipe-all-garbage: clean-pdfs
	/bin/bash ../clean-tex.sh
	cours.pdf
	clean
