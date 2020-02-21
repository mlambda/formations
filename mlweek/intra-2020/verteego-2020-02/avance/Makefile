title = title.pdf

intro := \
    about.pdf \
    nn-intro.pdf \
    nn-regularization.pdf \

keras := \
    keras-intro.pdf \

nn-keras-tp := \
    nn-keras-tp.pdf \

cnn := \
    cnn.pdf \
    cnn-keras.pdf \

cnn-keras-tp := \
    dpl-tp2.pdf \

rnn := \
    sequential-data.pdf \
    sequential-models.pdf \
    rnn.pdf \
    lstm.pdf \
    rnn-variants.pdf \
    langues.pdf \
    rnn-keras.pdf \

rnn-keras-tp := \
    dpl-tp3.pdf \

autoencoder := \
    autoencoder.pdf \

autoencoder-tp := \
    dpl-tp4.pdf \

eval-avance = evaluation-avance.pdf

debug := \
    cnn.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(keras) $(nn-keras-tp) $(rnn) $(rnn-keras-tp) $(cnn) $(cnn-keras-tp) $(autoencoder) $(autoencoder-tp) $(eval-avance)
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
