#!/bin/bash
#delete tmp files
#delete unused *tex acording to Makefile entries
rm *~
a=$(ls *tex)
b=$(grep "[^*%]\.pdf" Makefile | sed "s/[ \][ \]*$//g;s/^.*  *//g" | grep -v "(" | grep -v "cours" | sed "s/\.pdf/.tex/g" | sort | uniq)
rm $(echo -e "$a\n$b" | sort | uniq -ic | sort -n | grep -v " 2 " | sed "s/^.* //g")
