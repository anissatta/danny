#!/bin/sh 

olt_nam=$1
art_url=$2
art_tit=$3
art_lng=$4
dest=/home/prtza/kamsys/top/core

do_trans() {
	trans -b $1 "$art_tit"
}

case $art_lng in
    "en")
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
        ;;
    "ko")
        # Korean 
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
        echo $(do_trans ko:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ko:hi) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ko:ja) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "hi") 
        # Hindi 
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
        echo $(do_trans hi:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans hi:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans hi:ja) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "ja") 
        # Japanese 
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
        echo $(do_trans ja:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ja:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ja:hi) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    *)
        echo "Unexpected language code: $art_lng"
        ;;
esac

