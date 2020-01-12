.PHONY: all new clean
 
all: samplepaper.pdf

OPTIONS=-interaction nonstopmode -halt-on-error -file-line-error

new: clean all

%.pdf: %.tex *.bib
	pdflatex $(OPTIONS) $<
	- bibtex $*
	pdflatex $(OPTIONS) $<
	pdflatex $(OPTIONS) $<

clean:
	rm -f *.aux *.log *.bbl *.dvi *.pdf *.blg
