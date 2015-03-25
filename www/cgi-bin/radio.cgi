#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Radio</title>"
echo "<meta http-equiv=\"cache-control\" content=\"max-age=0\" />"
echo "<meta http-equiv=\"expires\" content=\"-1\" />"
echo "<meta http-equiv=\"pragma\" content=\"no-store\" />"
echo "</head>"
echo "<body>"
echo "<span id=radio>"
idx=`cat /www/index`
echo "`/usr/bin/awk \"NR == $idx\" /www/radio | cut -f1 -d\"|\" `"
echo "</span>"
echo "</body>"
echo "</html>"

