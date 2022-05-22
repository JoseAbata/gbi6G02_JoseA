#Determinar el número de filas (polinizadores) y columnas (plantas) de id1

##número de filas
cat $1 | wc -l > netsize.txt
#numero de columnas
head -n 1 $1 | wc -w >> netsize.txt

