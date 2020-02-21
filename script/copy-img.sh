#!/bin/bash
#
# Smart Copy all recognized img format from directories in arguments $@
# into the directory 'dest' below
#
#

dest="/home/fmg/formations-img"
extention="pdf png jpg jpeg gif svg pdf_tex"
for d in $@
do
    for ext in $extention
    do
	ls $d/*.$ext > /dev/null 2>&1
	if [ "$?" -eq "0" ]
	then
	    for f in $d/*.$ext
	    do
		d_name=$(basename $d)
		f_name=$(basename $f)
		echo $f
		f_ext=$(echo $f_name | grep -o "\.[^\.]*$")
		f_ext_lower=$(echo $f_ext | tr '[:upper:]' '[:lower:]')
		s_date=$(stat -c %Y "$f")
		#	echo $s_date
		s_date_human=$(stat -c %y "$f" | sed "s/ .*//")
		#	echo $s_date_human
		t_name=$(echo $f_name | sed "s/\.[^\.]*$//")$f_ext_lower
		c_name=$(echo $t_name | sed "s/\.[^\.]*$//")-$s_date_human$f_ext_lower
		t=$dest/$t_name
		c=$dest/$c_name
		if [ ! -f "$dest/$f_name" ]
		then
		    #copy target
		    echo Copie...
		    cp -p $f $t
		else
		    diff $t $f > /dev/null 2>&1
		    if [ "$?" -eq "1" ]
		    then
			#Si le fichier source est different, on renomme et on copie une version daté
			echo "---> Renomage de \"$t_name\" en \"$c_name\""
			cp -p $f $c
		    else
			echo Ok...
		    fi
		fi
	    done
	fi
    done
done
