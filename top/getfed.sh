#!/bin/sh 

olt_nam=$1
art_url=$2
art_tit=$3
art_lng=$4
dest=/home/user/kamsys/top/core

do_trans() {
	trans -b $1 "$art_tit"
}

if [ $art_lng = "en" ]; then

# English 
echo '' > $dest
echo '<p><span id="ocd">' >> $dest
echo $olt_nam >> $dest
echo '</span></p>' >> $dest

echo '<p><a id="url" href="#">' >> $dest
echo $art_url >> $dest
echo '</a></p>' >> $dest

echo '<p><h3>' >> $dest
echo $art_tit >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans en:ko) >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans en:hi) >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans en:ja) >> $dest
echo '</h3></p>' >> $dest

else
# Korean? 
echo '' > $dest
echo '<p><span id="ocd">' >> $dest
echo $olt_nam >> $dest
echo '</span></p>' >> $dest

echo '<p><a id="url" href="#">' >> $dest
echo $art_url >> $dest
echo '</a></p>' >> $dest

echo '<p><h3>' >> $dest
echo $art_tit >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans ko:hi) >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans ko:pt) >> $dest
echo '</h3></p>' >> $dest

echo '<p><h3>' >> $dest
echo $(do_trans ko:ja) >> $dest
echo '</h3></p>' >> $dest

fi
