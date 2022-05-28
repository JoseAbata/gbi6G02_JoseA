#!/bin/bash



edad=$1
sexo=$2

if [ "${edad}" -lt 18 ] || [ "${sexo}" -eq "chica" ]
then
	echo "$sexo menor de edad, tiene $edad años"
else
	echo "$sexo mayor de edad, tiene $edad años"
fi

