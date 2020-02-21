title = title.pdf

intro = about.pdf

qcm = qcm-initiation.pdf

debug.pdf: $(title) $(intro) $(debug)
	pdftk $+ cat output $@

slides.pdf: $(title) $(intro) $(qcm)
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
