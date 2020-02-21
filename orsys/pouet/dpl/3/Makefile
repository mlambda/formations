title = title.pdf

intro := \
    about.pdf \

rnn := \
    sequential-data.pdf \
    sequential-models.pdf \
    rnn.pdf \
    lstm.pdf \
    rnn-variants.pdf \
    langues.pdf \
    rnn-keras.pdf \

autoencoder := \
    autoencoder.pdf \

rnn-keras-tp := \
    dpl-tp3.pdf \

autoencoder-tp := \
    dpl-tp4.pdf \

debug := \
    cnn.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(rnn)  $(rnn-keras-tp) $(autoencoder) $(autoencoder-tp)
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
