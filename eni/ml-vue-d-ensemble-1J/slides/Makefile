title = title.pdf

intro := \
    0-about.pdf \
    0-historique-ia.pdf

possibilities := \
    1-machine-learning.pdf \
    1-data.pdf \
    1-learn.pdf \
    1-NN.pdf \
    1-vision.pdf \
    1-RNN.pdf \
    1-langues.pdf \
    1-petit-jeu.pdf \
    1-GAN.pdf \
    1-RL.pdf \
    1-RL-deep.pdf \
    1-problematiques.pdf \
    1-AlphaGo.pdf

actors := \
    3-gafa.pdf \
    3-startup.pdf \
    3-chine.pdf

ia-in-motion := \
    4-tendencies-and-new-sectors.pdf \
    4-transport.pdf \
    4-sante.pdf \
    4-coding.pdf

machine-learning-craftmanship := \
    ml-craftmoncul.pdf

machine-learning-craftmanship_debug := \
    5-ml-craftmanship.pdf

questions = questions.pdf

tagada = \
    1-problematiques.pdf \
    4-tendencies-and-new-sectors.pdf \
    4-transport.pdf \
    4-sante.pdf \
    4-coding.pdf

questions = questions.pdf

slides.pdf: $(title) $(intro) $(possibilities) $(machine-learning-craftmanship) $(actors) $(ia-in-motion) $(questions)
	pdftk $+ cat output $@

actors.pdf: $(title) $(actors)
	pdftk $+ cat output $@

pouet.pdf: $(title) $(tagada)
	pdftk $+ cat output $@

debug.pdf: $(title) $(ia-in-motion)
	pdftk $+ cat output $@

%.pdf: %.tex formation.cls
	latexmk $<

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc *.vrb *.vrb~ _minted*

clean-pdfs: clean
	rm -rf *.pdf

.PHONY: clean
