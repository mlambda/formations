#!/bin/bash
cur_dir=$(pwd)
temp=/nas/data/FORMATIONS/slides/script/starter-files
if [ $# -gt 0 ]
then
    nbjours=$1
else
    nbjours=1
fi
    
#On vérifie que le dossier n'existe pas déjà
for i in $(seq 1 $nbjours)
do
    cd $cur_dir
    target_dir=$cur_dir/$i
    if [ ! -d $target_dir ]
    then
	#Create target formation project directory ready to compile latex with acces to template and img folder
	
	#Create Directory
	echo "Create : $target_dir"
	mkdir $target_dir && cd $target_dir
	#Create symbolic link
	ln -s /nas/data/FORMATIONS/slides/img/ img && echo "created : img/"
	ln -s /nas/data/FORMATIONS/slides/template template && echo "created : templates/"
	ln -s /nas/data/FORMATIONS/slides/code-illustration code-illustration && echo "created : code-illustration/"
	#Copy MakeFile and formations.cls
	cp -p $temp/Makefile.temp Makefile && echo "created : "Makefile
	cp -p $temp/formation.cls . && echo "created : "formation.cls
	
	#Copy first tex files
	tex_files=$(grep "\.pdf" Makefile | sed "s/ /\n/g" | grep pdf | grep -v ":" | grep -v "*" | sed "s/\..*/.tex/g" | sort | uniq )
	for f in $tex_files
	do
	    if [ ! -e $f ]
	    then
		cp $temp/$f $f && echo "created : "$f
	    fi
	done
	#Copy make-tex.sh script
	cp -p $temp/make-tex.sh . && echo "created : make-tex.sh"
	#Copy make-tex.sh script
	cp -p $temp/clean-tex.sh . && echo "created : clean-tex.sh"
    else
	echo "$tnarget_dir"
	echo "Already exist !, clean it if necessary before re-trying"
    fi
done
