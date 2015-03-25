#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Song</title>"
echo "<meta http-equiv=\"cache-control\" content=\"max-age=0\" />"
echo "<meta http-equiv=\"expires\" content=\"-1\" />"
echo "<meta http-equiv=\"pragma\" content=\"no-store\" />"
echo "</head>"
echo "<body>"
echo "<span id=song>"

song=`tail -1 /tmp/title | cut -d':' -f2 | xargs -0`
if [ -z "$song" ]
then
  song="No song info"
fi
echo "$song"
echo "</span>"
echo "</body>"
echo "</html>"

