#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Connect</title>"
echo "<meta name='viewport' content='width=320px, initial-scale=1, maximum-scale=1'>"
echo "<META HTTP-EQUIV='refresh' CONTENT='30'>"
echo "<link href='../css/style.css' rel='stylesheet' type='text/css' media='all' />"

echo "</head><body>"
iface=`uci show wireless | grep mode=sta | cut -d"." -f2`
curr_encr=`uci get wireless.$iface.encryption`
list=`iw dev wlan0 scan | grep SSID | cut -d":" -f2 | cut -d" " -f2`
nr=`printf "%b\n" $list | wc -l`
connectedto=`iw dev wlan0 link | grep SSID | cut -d":" -f2`
echo "Now connected to:$connectedto<BR>"
echo "Connect to SSID:<BR>"
echo "<FORM ACTION='/cgi-bin/conn.cgi'>"
echo "<select name=selected>"
for i in `seq $nr`
do
 SSID=`printf '%b\n' $list | awk 'NR=='$i'{print;exit}'`
 if [ $SSID = $connectedto ];
 then
  echo "<option selected=true>$SSID"
 else
  echo "<option>$SSID"
 fi
done
echo "</select><BR>"
echo "Password: <BR><INPUT type='password' name='passwd' size=20%><BR>"
if [ $curr_encr = "psk2" ];
then
 echo "<input type='radio' name='auth' value='psk2' checked='true'>WPA2<br>"
else
 echo "<input type='radio' name='auth' value='psk2'>WPA2<br>"
fi
if [ $curr_encr = "psk" ];
then
 echo "<input type='radio' name='auth' value='psk' checked='true'>WPA<br>"
else
 echo "<input type='radio' name='auth' value='psk'>WPA<br>"
fi
if [ $curr_encr = "wep+shared" ];
then
 echo "<input type='radio' name='auth' value='wep+shared' checked='true'>WEP+Shared key<br>"
else
 echo "<input type='radio' name='auth' value='wep+shared'>WEP+Shared key<br>"
fi
if [ $curr_encr = "wep+open" ];
then
 echo "<input type='radio' name='auth' value='wep+open' checked='true'>WEP+Open<br>"
else
 echo "<input type='radio' name='auth' value='wep+open'>WEP+Open<br>"
fi
if [ $curr_encr = "none" ];
then
 echo "<input type='radio' name='auth' value='none' checked='true'>OPEN<br>"
else
 echo "<input type='radio' name='auth' value='none'>OPEN<br>"
fi 
echo "<INPUT TYPE=SUBMIT VALUE='Connect&Save'>"
</FORM>

echo "</body>"
echo "</html>"

