#!/bin/bash

# For run : ./script-v3.sh filename
# NOTE : filename should be without extension for example ./script-v3.sh test2
# This file puts all the png files in a tex file and compiles it 

cp test.tex $1.tex	# $1 reads the 1st argument
count=1
for f in *.pdf; do
    filename=$(basename  "$f")
    filename=${filename%.*}
    filename=${filename//_/ }
    echo $filename
    echo $f
    perl -spe 's/intime_mean_pu.pdf/$a/;
    s/TitleFrame/$b/' < fig.tex -- -a="$f" -b="$filename" > "fig_$count.tex"

    sed -i "/Pointer-rk/r fig_$count.tex" "$1.tex"
    ((++count))
done
pdflatex $1.tex
pdflatex $1.tex
#rm $1.tex
rm fig_*.tex  $1.toc $1.snm $1.out $1.nav $1.aux $1.log
gnome-open $1.pdf
echo "Finished."
