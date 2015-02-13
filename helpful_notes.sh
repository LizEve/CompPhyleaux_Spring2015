#!/bin/bash

-ADD EXTENSION
	for f in jmodg_*; do mv "$f" "$f.nex"; done
-REMOVE EXTENSION
	for f in jmodg_*.nex; do mv "$f" "${f%.*}"; done
!Helpful bash syntax info
	-http://www.tldp.org/LDP/abs/html/parameter-substitution.html#PSOREX1
