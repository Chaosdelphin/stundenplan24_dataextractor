import xml.etree.ElementTree as ET
import sys
from xml.sax.saxutils import escape
reload(sys)
sys.setdefaultencoding('utf8')
try:
	tree = ET.parse('vpandaten.xml')
except:
	print "<html><head><meta http-equiv='refresh' content='60' ><link rel='stylesheet' href='style.css'><title>No data</title></head><body><br><br><br><br><br><br><center><h1> Kein Plan heute... </h1></center></body></html>"
	exit(0)
root = tree.getroot()
count=0
splitthreshhold=40
split=0
for items in root.iter('aktion'):
	count=count+1
if count > splitthreshhold:
	split=1
index=0
titel=""
for items in root.iter('kopf'):
	titel=escape(str(ET.tostring(items.find('titel'), encoding="UTF-8", method="text")))
print "<html><head><meta http-equiv='refresh' content='300' charset='utf-8'><link rel='stylesheet' href='style.css'><title>Vertretungsplan "+titel+"</title>"
print "<script type='text/javascript' src='http://code.jquery.com/jquery-latest.min.js'>"
print "</script><script type='text/javascript' src='autoscroll.js'></script>"
print "<script type='text/javascript' src='endless.js'></script>"
#print "<script type='text/javascript'>$('body,html').animate({scrollTop: 0}, 40);</script>"
print "<script type='text/javascript'>$(document).ready(function(){$(document).endless({direction:'up', scrollbar:'disable',append:function(){}});});</script>"

print "</head><body>"
print "<center><h1>Vertretungsplan "+titel+"</h1></center>"
if split == 0:
	print "<table class='stat' style='width:100%' border='1' align='left'><tr><b><th>Klasse</th><th>Stunde</th><th>Fach</th><th>Lehrer</th><th>Raum</th><th>Info</th></b></tr>"
else:
	print "<table class='stat' style='width:49%' border='1' align='left'><tr><b><th>Klasse</th><th>Stunde</th><th>Fach</th><th>Lehrer</th><th>Raum</th><th>Info</th></b></tr>"
for items in root.iter('aktion'):
	print "<tr>"
	print "<td style='white-space:nowrap;'>"+escape(str(ET.tostring(items.find('klasse'), encoding="UTF-8", method="text")))+"</td>"
	print "<td>"+escape(str(ET.tostring(items.find('stunde'), encoding="UTF-8", method="text")))+"</td>"
	print "<td>"+escape(str(ET.tostring(items.find('fach'), encoding="UTF-8", method="text")))+"</td>"
	print "<td>"+escape(str(ET.tostring(items.find('lehrer'), encoding="UTF-8", method="text")))+"</td>"
	print "<td>"+escape(str(ET.tostring(items.find('raum'), encoding="UTF-8", method="text")))+"</td>"
	print "<td>"+escape(str(ET.tostring(items.find('info'), encoding="UTF-8", method="text")))+"</td>"
	print "</tr>"
	index=index+1
	if index==count/2:
		if split == 1:
			print "<table class='stat' style='width:49%' border='1' align='right'><tr><b><th>Klasse</th><th>Stunde</th><th>Fach</th><th>Lehrer</th><th>Raum</th><th>Info</th></b></tr>"

print "<tr><b><th>Klasse</th><th>Stunde</th><th>Fach</th><th>Lehrer</th><th>Raum</th><th>Info</th></b></tr></table>"
#print "<center><h1>Vertretungsplan "+titel+"</h1></center>"
#print "<div id='end'>ende</div>"
print "</script><script type='text/javascript' src='autoscroll2.js'>downscroll();</script>"

#print "<script type='text/javascript' src='http://code.jquery.com/jquery-latest.min.js'></script><script type='text/javascript' src='autoscroll.js'></script>"
#print "<script type='text/javascript' src='endless.js'></script>"
#print "<script type='text/javascript'>$(document).ready(function(){$(document).endless({direction:'vertical'});});</script>"
print "</body></html>"
