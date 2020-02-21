intro := \
    0-about.pdf \
    0-rappels.pdf \

cours := \
    1-dimensionality-reduction.pdf \
    1-pca-lda.pdf \
    1-autoencoder-embeddings.pdf \
    1-images.pdf \
    1-convolution-pooling.pdf \
    1-petit-jeu.pdf \
    1-GAN.pdf	

title = title.pdf 

questions = questions.pdf 


cours.pdf: $(title)  $(intro) $(cours)
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
