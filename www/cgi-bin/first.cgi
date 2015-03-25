#!/bin/sh
count=`cat /www/radio | wc -l`
echo 1 > /www/index
index=`cat /www/index`
killall gst-launch-0.10
url=`awk "NR == $index" /www/radio | cut -f2 -d"|"`
gst-launch -t playbin uri=$url | awk /title:/ | tee /tmp/title &

#Redirect the browser back to the index page
 echo "Content-type: text/html"
 echo ""
 echo "<html><head><title>Remote control</title>"
 echo "</head><body>"
 echo "<script type="text/javascript"><!--"
 echo "setTimeout('Redirect()',0);"
 echo " function Redirect(){  location.href = './index.cgi';}"
 echo " --></script></body></html>"