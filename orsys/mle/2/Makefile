title = title.pdf

intro := \
    about.pdf \

ia-in-motion := \
    community.pdf \
    gafa.pdf \
    startup.pdf \
    chine.pdf \
    tendencies-and-new-sectors.pdf \
    transport.pdf \
    sante.pdf \
    coding.pdf \

machine-learning-craftmanship := \
    ml-tools.pdf \
    ml-craftmoncul.pdf \

ml-law := \
    problematiques.pdf \
    ml-ethique.pdf \
    ml-juridique.pdf \

questions = questions.pdf


slides.pdf: $(title) $(intro) $(historique) $(data-ml) $(ia-in-motion) $(machine-learning-craftmanship) $(ml-law) $(questions)
	pdftk $+ cat output $@

actors.pdf: $(title) $(actors)
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
