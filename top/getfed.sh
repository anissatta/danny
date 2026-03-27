#!/bin/sh 

olt_nam=$1
art_url=$2
art_tit=$3
art_lng=$4
dest=/home/user/kamsys/top/core

do_ask() {
	/home/user/kamsys/top/tomo.py "$1"
}

do_trans() {
	trans -b $1 "$art_tit"
}

echo '' > $dest
echo '<script>' >> $dest
echo "document.getElementById('mybody').className = '${olt_nam}';" >> $dest
echo '</script>' >> $dest

case $art_lng in
    "en")
        # English 
        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans en:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans en:ja) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$art_tit") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "ko")
        # Korean 
        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans ko:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ko:ja) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$(do_trans ko:en)") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "hi") 
        # Hindi 
        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans hi:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans hi:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans hi:ja) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "ja") 
        # Japanese 
        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans ja:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans ja:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$(do_trans ja:en)") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    *)
        echo "Unexpected language code: $art_lng"
        ;;
esac

