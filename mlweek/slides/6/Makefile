intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-sequential-data.pdf \
    1-sequential-models.pdf \
    1-sequential-first-approach.pdf \
    1-markov.pdf \
    1-hmm.pdf \
    1-rnn.pdf \
    1-lstm.pdf \
    1-rnn-variants.pdf \
    1-tp-review.pdf \

title = title.pdf 

questions = questions.pdf 


cours.pdf: $(title)  $(intro) $(cours) $(questions)
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
