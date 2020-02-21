intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-tp-review.pdf \
    1-nlp.pdf \
    1-attention-model.pdf \
    1-memory-network.pdf \
    1-transformer-networks.pdf \
    1-tensorflow.pdf \
    1-tp-on-code.pdf \

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
