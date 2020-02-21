#!/bin/bash
#
# Smart Copy all *.tex from directories in arguments $@
# into the directory 'dest' below
#
#
dest="/nas/data/FORMATIONS/slides/template/orsys"
for d in $@
do
    for f in $d/*tex
    do	
	d_name=$(basename $d)
	f_name=$(basename $f)
	s_date=$(stat -c %Y "$f")
	s_date_human=$(stat -c %y "$f" | sed "s/ .*//")
	t_name=$(echo $f_name | sed "s/^[0-9][0-9]*-//" | sed "s/.tex$//" | tr '[:upper:]' '[:lower:]')
	c_name=$(echo $t_name | sed "s/.tex$//")
	t=$dest/$t_name.tex
	c=$dest/$c_name-$s_date_human.tex
	if [ ! -f $t ]
	then
	    #copy target
	    cp -p $f $t && echo "copy $t"
	else
	    t_date=$(stat -c %Y "$t")
	    if [ "$s_date" -gt "$t_date" ]
	    then
		#Si le fichier source est plus récent, on update la target
		t_date_human=$(stat -c %y "$t" | sed "s/ .*//")
		t_tmp=$dest/$t_name-$t_date_human.tex
		echo "$t_name.tex plus récent"
		mv $t $t_tmp && echo "---> $t_tmp sauvegardé"
		cp -p $f $t && echo "---> copy $t"
	    fi
	fi
	if [ ! -f $c ]
	then
	    #copy dated-copy if différent from main file
	    diff $f $t || cp -p $f $c && echo "copy $c"
	fi
    done
done
