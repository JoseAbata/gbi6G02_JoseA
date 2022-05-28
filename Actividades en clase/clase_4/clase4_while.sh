#!/bin/bash


dividendo=$1
divisor=$2
cambio=$3
while [ $dividendo -le 100 ]
do
	x=$dividendo/$divisor
	echo "la division entre $dividendo y $divisor es $x"
	dividendo=$(( dividendo+$cambio ))
done

