title = title.pdf

nn := \
    nn-intro.pdf \
    nn-cnn.pdf \

tp1 := \
    tp-nn.pdf \
    tp-cnn.pdf \

rnn := \
    sequential-data.pdf \
    sequential-models.pdf \
    markov-model.pdf \
    hmm-latest.pdf \
    rnn.pdf \
    lstm.pdf \
    rnn-variants.pdf \
    langues.pdf \
    rnn-keras.pdf \

tp2 := \
    tp-rnn.pdf \

autoencoder := \
    autoencoder.pdf \

tp3 := \
    tp-autoencoder.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(nn) $(tp1) $(rnn) $(tp2) $(autoencoder) $(tp3)
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
