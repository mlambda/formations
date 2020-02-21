#!/bin/bash
#create necessary *tex template from *pdf entries in Makefile.
#Already existant *tex files are untouched
l=$(grep "\.pdf" Makefile | sed "s/ /\n/g" | grep pdf | grep -v ":" | grep -v "*" | sed "s/\..*/.tex/g" | sort | uniq )
for f in $l
do
    if [ ! -e $f ]
    then
	template=template/cours/$f
	if [ ! -e $template ]
	then
	    cp template.tex $f && echo created empty template" : "$f
	else
	    cp $template $f && echo created cours template" : "$f
	fi
    fi
done
