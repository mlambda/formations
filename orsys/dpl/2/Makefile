title = title.pdf

intro := \
    about.pdf \

keras := \
    keras-intro.pdf \

cnn := \
    nn-cnn.pdf \
    cnn-keras.pdf \

cnn-keras-tp := \
    dpl-tp2.pdf \

debug := \
    cnn.pdf \

questions = questions.pdf

debug.pdf: $(title) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(keras) $(cnn) $(questions) $(cnn-keras-tp)
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
