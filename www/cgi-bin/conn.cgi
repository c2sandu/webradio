#!/bin/sh
iface=`uci show wireless | grep mode=sta | cut -d"." -f2`
ssid=`echo $QUERY_STRING | cut -d"&" -f1 | cut -d"=" -f2`
passwd=`echo $QUERY_STRING | cut -d"&" -f2 | cut -d"=" -f2`
encr=`echo $QUERY_STRING | cut -d"&" -f3 | cut -d"=" -f2`

uci set wireless.$iface.ssid=$ssid
uci set wireless.$iface.key=$passwd
uci set wireless.$iface.encryption=$encr

uci commit wireless
wifi
sleep 5

#Redirect the browser back to the connection page
 echo "Content-type: text/html"
 echo ""
 echo "<html><head><title>Connect</title>"
 echo "</head><body>"
 echo "<script type="text/javascript"><!--"
 echo "setTimeout('Redirect()',0);"
 echo " function Redirect(){  location.href = './connect.cgi';}"
 echo " --></script></body></html>"

echo "</body>"
echo "</html>"

