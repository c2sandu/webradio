#!/bin/sh
cgi_decodevar ()
{
    [ $# -ne 1 ] && return
    local v t h
    # replace all + with whitespace and append %%
    t="${1//+/ }%%"
    while [ ${#t} -gt 0 -a "${t}" != "%" ]; do
	v="${v}${t%%\%*}" # digest up to the first %
	t="${t#*%}"       # remove digested part
	# decode if there is anything to decode and if not at end of string
	if [ ${#t} -gt 0 -a "${t}" != "%" ]; then
	    h=${t:0:2} # save first two chars
	    t="${t:2}" # remove these
	    v="${v}"`echo -e \\\\x${h}` # convert hex to special char
	fi
    done
    # return decoded string
    echo "${v}"
    return
}

radio=`echo $QUERY_STRING | awk -F'=' '{ print $2 }'`
radio=`cgi_decodevar $radio`
name=`echo $QUERY_STRING | awk -F'=' '{ print $3 }'`

if echo $radio | grep -q ".pls";
then
  radio=`wget -qO - $radio | grep File1 | cut -d"=" -f2`
else
   if echo $radio | grep -q ".m3u";
   then
       radio=`wget -qO - $radio | grep -v -m1 "^#"`
   else
       if echo $radio | grep -q ".xspf";
       then
            radio=`wget -qO - $radio | awk -F"<location>" '{print $2}' | awk -F"</location>" '{print $1}'`

       fi
   fi
fi
echo $radio
#cgi_decodevar $radio
echo `cgi_decodevar $name`"|"`cgi_decodevar $radio` >> /www/radio

#echo $temp >> /www/radio

#Redirect the browser back to the index page
 echo "Content-type: text/html"
 echo ""
 echo "<html><head><title>Remote control</title>"
 echo "</head><body>"
 echo "<script type="text/javascript"><!--"
 echo "setTimeout('Redirect()',0);"
 echo " function Redirect(){  location.href = './index.cgi';}"
 echo " --></script></body></html>"
