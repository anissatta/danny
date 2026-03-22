#!/bin/sh 

dest=/home/user/kamsys/bottom/core

trans2ja() {
	trans -b en:ja "$1"
}

echo '' > $dest

for i in "$@"; do
    echo '<li>' >> $dest
    echo $(trans2ja "$i") >> $dest
    echo "(<i>${i}</i>)" >> $dest
    echo '</li>' >> $dest
done

