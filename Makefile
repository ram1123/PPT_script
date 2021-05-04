all: tex pdf open

tex:
	./MakePPT.sh

pdf:
	pdflatex ppt_test.tex

open:
	gnome-open ppt_test.pdf

clean:
	rm -f *.toc *.snm *.out *.nav *.aux *.log *.vrb *.pyc

cleanall:
	rm -f *.toc *.snm *.out *.nav *.aux *.log *.vrb *.pyc *.pdf
