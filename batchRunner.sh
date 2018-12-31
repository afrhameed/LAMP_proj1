#!/bin/sh
# creates an xml file for a stocks website every minute for an hour
# and then calls a python script to load stock information onto mysql

i=0
while [ $i -lt 60 ]
do
	echo $i
	Date=$(date +'%Y-%m-%d-%H-%M-%S')
	date1=${Date}.html
	date2=${Date}.xhtml
	curl -o $date1 http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html 
	java -jar tagsoup-1.2.1.jar --files $date1
	touch ${Date}.csv
	python xhtmltosql.py $date2 > ${Date}.csv
	i=$((i+1))
	sleep 60
done

