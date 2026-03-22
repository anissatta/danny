#!/bin/sh 

url=$1
tit=$2
lng=$3
dest=/home/user/kamsys/right/core

do_trans() {
	trans -b $1 "$tit"
}

case $lng in
    "en")
        # English
        echo '' > $dest
        echo '<p><a id="url" href="#">' >> $dest
        echo $url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans en:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans en:ja) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "ko")
        # Korean 
        echo '' > $dest
        echo '<p><a id="url" href="#">' >> $dest
        echo $url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ko:en) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_trans ko:ja) >> $dest
        echo '</h3></p>' >> $dest
        ;;
    *)
        echo "Unexpected language code: $lng"
        ;;
esac

