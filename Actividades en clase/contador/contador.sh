cut -d ";" -f 2 $1 | tail -n +2 | sort | uniq -c | sort > $2
cut -d ";" -f 3 $1 | tail -n +2 | sort | uniq -c | sort >> $2
cut -d ";" -f 4 $1 | tail -n +2 | sort | uniq -c | sort >> $2
