#!/bin/bash
#create necessary *tex template from *pdf entries in Makefile.
#Already existant *tex files are untouched
a=$(grep "\.pdf" Makefile | sed "s/ /\n/g" | grep pdf | grep -v ":" | grep -v "*" | sed "s/\..*/.tex/g")
for f in $a; do if [ ! -e $f ]; then cp template.tex $f && echo created" : "$f; fi; done
