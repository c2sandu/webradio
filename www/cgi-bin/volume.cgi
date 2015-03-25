#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Radio</title>"
echo "<meta http-equiv=\"cache-control\" content=\"max-age=0\" />"
echo "<meta http-equiv=\"expires\" content=\"-1\" />"
echo "<meta http-equiv=\"pragma\" content=\"no-store\" />"
echo "</head>"
echo "<body>"
echo "<span id=volume>"

fl=`amixer get Speaker | awk /"Front Left:"/`
vol="Now playing (volume <span style='color:blue'>"`echo $fl | xargs -0 | cut -d' ' -f5`"</span>"
case "$fl" in 
  *\[off\]*)
    vol=$vol" - <span style="color:red">muted</span>):"
;;
  *\[on\]*)
    vol=$vol" - <span style="color:blue">unmuted</span>):"
;;
esac
echo "$vol"
echo "</span>"
echo "</span>"
echo "</body>"
echo "</html>"

