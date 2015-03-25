#!/bin/sh
index=`cat /www/index`
#awk "NR != $index" /www/radio
sed -i "$index d" /www/radio
count=`cat /www/radio | wc -l`
if [ $index -ge $count ]; then
 echo 1 > /www/index;
else
let z=$index+1;
echo $z > /www/index;
fi
killall gst-launch-0.10
index=`cat /www/index`
gst-launch -t playbin uri=$url | awk /title:/ | tee /tmp/title &
#gst-launch playbin uri=$url &
gst-launch -t playbin uri=$url | tee /tmp/title &
#Redirect the browser back to the index page
 echo "Content-type: text/html"
 echo ""
 echo "<html><head><title>Remote control</title>"
 echo "</head><body>"
 echo "<script type="text/javascript"><!--"
 echo "setTimeout('Redirect()',0);"
 echo " function Redirect(){  location.href = './index.cgi';}"
 echo " --></script></body></html>"