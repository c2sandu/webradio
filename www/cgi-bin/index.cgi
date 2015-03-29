#!/bin/sh
echo Content-type: text/html
echo ""
echo "<head>"
echo "<title>Remote control</title>"
echo "<link href='../css/style.css' rel='stylesheet' type='text/css' media='all' />"
echo "<meta name="viewport" content='initial-scale=1'>"
echo "<meta charset='utf-8'>"
echo "<meta http-equiv=\"cache-control\" content=\"max-age=0\" />"
echo "<meta http-equiv=\"expires\" content=\"-1\" />"
echo "<meta http-equiv=\"pragma\" content=\"no-cache\" />"

song=`tail -1 /tmp/title | cut -d':' -f2 | xargs -0`

echo "<script type='text/javascript' src='../js/jquery-1.11.2.min.js'></script>"
echo "<script>"
echo "\$(document).ready(function(){"
echo "	setInterval(function() {"
echo "        \$('#song').load('song.cgi?random=`echo $(</dev/urandom tr -dc 0-9 | dd bs=5 count=1)` #song');"
echo "        \$('#radio').load('radio.cgi?random=`echo $(</dev/urandom tr -dc 0-9 | dd bs=5 count=1)` #radio');"
echo "        \$('#volume').load('volume.cgi?random=`echo $(</dev/urandom tr -dc 0-9 | dd bs=5 count=1)` #volume');"
echo "    }, 3000);"
echo "});"
echo "</script>"


echo "</head>"
echo "<body>"

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

echo "<span id=volume>$vol</span><BR>"

index=`cat /www/index`
url=`awk "NR == $index" /www/radio | cut -f2 -d"|"`

if [ -z "$song" ]
then
  song="No song info"
fi


echo "<a href='"
echo $url
echo "'><h3 class='header'><center><span id='radio'>"
/usr/bin/awk "NR == `cat /www/index`" /www/radio | cut -f1 -d"|" 
echo "</span>"
echo "<BR><span style='color:red'>&#x266B; </span><span id='song'>$song</span><span style='color:red'> &#x266B;</span>"
echo "</center></h3></a>"


/bin/cat << EOM
<table align="center" style="margin: 0px auto;">
<tr>
<td><a href="./mute.cgi"><img src="../images/mute.png" border="0" alt="Mute"></a></td>
<td><a href="./volume_up.cgi"><img src="../images/volume_up.png" border="0" alt="Volume up"></a></td>
<td><a href="./volume_down.cgi"><img src="../images/volume_down.png" border="0" alt="Volume down"></a></td>
</tr>
<tr>
<td><a href="./previous.cgi"><img src="../images/previous.png" border="0" alt="Previous radio station"></a></td>
<td><a href="./play_pause.cgi"><img src="../images/play_pause.png" border="0" alt="Play/Pause"></a></td>
<td><a href="./next.cgi"><img src="../images/next.png" border="0" alt="Next radio station"></a></td>
</tr>
<tr>
<td align="center"><a href="./first.cgi" alt="Go to the first radio on the list" style="font-size:400%"><<</a></td>
<td></td>
<td align="center"><a href="./last.cgi" alt="Go to the last radio on the list" style="font-size:400%">>></a></td>
</tr>
</table>
<a href="../add.html");">Add a new radio to list</a> <BR>
<a href="./remove.cgi" onclick="if (!confirm('Are you sure you want to remove the current radio from the list?')) return false;">Remove this radio from list</a><BR>
<a href="../connect.html");">Change WiFi network connection</a> <BR>
</body>
</html>

EOM
