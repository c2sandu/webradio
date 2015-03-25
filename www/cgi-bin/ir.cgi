#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Suggestions from Internet Radio</title>"
echo "<meta name='viewport' content='width=320px, initial-scale=1, maximum-scale=1'>"
echo "<link href='../css/style.css' rel='stylesheet' type='text/css' media='all' />"

echo "</head><body>"
link=`echo $QUERY_STRING| awk -F"&&" '{print $1}'`
title=`echo $QUERY_STRING| awk -F"&&" '{print $2}'`
wget -q -O - $link | grep pls | grep FLA | grep "http://.*.pls" | awk -F"title=" '{print $2}' | awk -F"&amp;website=" '{print $1}' >/tmp/stations
wget -q -O - $link | grep pls | grep FLA | grep "http://.*.pls" | awk -F"mount=" '{print $2}' | awk -F"&amp" '{print $1}' >/tmp/links
nr=`wc -l < /tmp/stations`
echo "<h2>$title</h2>"
echo "<ul>"
for i in `seq $nr`
do
  echo "<li><a href=`awk 'NR=='$i'{print;exit}' /tmp/links`>`awk 'NR=='$i'{print;exit}' /tmp/stations`</a></li>"
done
echo "</ul>"
echo "</body>"
echo "</html>"

