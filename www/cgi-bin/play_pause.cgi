#!/bin/sh
amixer sset 'Speaker' toggle &
logger "Mute by play/pause"

#Redirect the browser back to the index page
 echo "Content-type: text/html"
 echo ""
 echo "<html><head><title>Remote control</title>"
 echo "</head><body>"
 echo "<script type="text/javascript"><!--"
 echo "setTimeout('Redirect()',0);"
 echo " function Redirect(){  location.href = './index.cgi';}"
 echo " --></script></body></html>"
