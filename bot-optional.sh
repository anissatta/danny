#!/bin/sh

FRS=3
XFRS=3

annt_msg() {
	convert bot_temp.png -font ./DungGeunMo.ttf -gravity NorthWest -pointsize 24 -stroke navy -annotate +132+16 "$1" bot_temp.png
}

h=$(date +"%k")

if [ $h -gt 4 ] && [ $h -lt 17 ]; then
	composite -geometry +8+8 pix/w$(($1%4)).xpm bot_temp.png bot_temp.png
else
	composite -geometry +8+8 pix/m$(($1%4)).xpm bot_temp.png bot_temp.png
	# food CF at night :) 
	composite -gravity SouthEast -geometry +0+0 cf/fr$(printf %03d $(($1%$FRS))).png bot_temp.png bot_temp.png
fi

# make semi-transparent 
convert bot_temp.png -alpha set -channel A -evaluate set 60% bot_temp.png

# auto-insa :) 
if [ $h -gt 2 ] && [ $h -lt 8 ]; then
    annt_msg "안녕하세요?"
fi
if [ $h -gt 14 ] && [ $h -lt 20 ]; then
    annt_msg "안녕히 주무세요, 저의 고양이."
fi

# another one. 
cat /home/user/kamsys/right/head.html /home/user/kamsys/right/core /home/user/kamsys/right/tail.html > /home/user/kamsys/right/index.html 
wkhtmltoimage  --width 800 --crop-h 480 /home/user/kamsys/right/index.html right.png
# another food CF at night :) 
if [ $h -lt 5 ] || [ $h -gt 16 ]; then
    composite -gravity North -geometry +0+250 xcf/n$(printf %03d $(($1%$XFRS))).png right.png right.png
fi
# make semi-transparent 
convert right.png -alpha set -channel A -evaluate set 60% right.png
# make semi-transparent 
convert fright.png -alpha set -channel A -evaluate set 60% fright.png

# another one #2. 
cat /home/user/kamsys/top/head.html /home/user/kamsys/top/core /home/user/kamsys/top/tail.html > /home/user/kamsys/top/index.html 
wkhtmltoimage --width 1920 --crop-h 214 /home/user/kamsys/top/index.html top.png
# make semi-transparent 
convert top.png -alpha set -channel A -evaluate set 60% top.png

