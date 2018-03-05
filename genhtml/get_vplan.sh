#!/bin/bash
date=$(date +'%Y%m%d')
passwd=""
user=""
schoolnumber=""
#date=20180305
cd /root/gschumannvplan
wget -N https://$user:$passwd@www.stundenplan24.de/$schoolnumber/vplan/vdaten/VplanKl$date.xml -O vpandaten.xml
python vplan_html.py > ../html/vplan.html

