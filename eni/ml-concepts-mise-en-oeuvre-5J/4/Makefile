modules-d1 := \
    1-features-and-modeling.pdf \
    3-NN.pdf \
    1-autoencoder-embeddings.pdf \
    1-images.pdf \
    1-convolution-pooling.pdf \
    1-petit-jeu.pdf \
    1-GAN.pdf \
    1-sequential-data.pdf \
    1-sequential-models.pdf \
    1-rnn.pdf \
    1-lstm.pdf \
    1-rnn-variants.pdf \
    1-nlp.pdf \
    1-attention-model.pdf \
    1-memory-network.pdf \
    1-transformer-networks.pdf \
    1-tensorflow.pdf \

title = title.pdf

tp = tp.pdf

questions = questions.pdf

slides.pdf: $(title) $(modules-d1) $(tp)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
