#!/bin/bash
for file in $1/*.fasta
do
	echo "$file"
	cat $file | wc
done
