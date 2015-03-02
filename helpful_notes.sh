#!/bin/bash

-add file extensions recursively 
	for f in jmodg_*; do mv "$f" "$f.nex"; done
	filler line

-remove file extensions recursively 
	for f in jmodg_*.nex; do mv "$f" "${f%.*}"; done
	filler line

-move files into folders according to name
	for f in *.nex; do base=`basename $f .nex`; cd $base; mv "../jmodg_$base" . ; cd ../ ; done
	for f in *.nex;  do base=`basename $f .nex`; cd $base; cp "../$base.nex" .; cd ../; done

-iterate through files, run program
	for f in squamg_*; do cd $f; Garli-2.0 -b $f.garli.conf; cd ../;done

-move all files up a folder
	for f in *.nex; do cp ./$f ../$f; done
-compare files 
	for f in squamg_*; do cd $f; cmp --silent $old $new || echo "files are different" ; cd ../;done

-rename and move files

	for f in squamg_*;
	do
	cd $f 
	cp 'mpi_messages.log' $f'.mpi_messages.log'
	mv $f'.mpi_messages.log' ../log_outputs/mpi_run.2.23.15
	cd ../
	done

====GREP=====

-pull out one line of all the files, all the folders with a string
	grep -C 1 "Time used" squamg_*/*






=====___LINKS____================================================================================================

!Helpful bash syntax info
	-http://www.tldp.org/LDP/abs/html/parameter-substitution.html#PSOREX1
