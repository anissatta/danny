#!/bin/sh

WTI=$(w3m -dump https://oilprice.com/| grep "WTI Crude")
FORTUNE=$(fortune -s)

convert bottom_base.png -font ./DungGeunMo.ttf -gravity NorthWest -pointsize 32 +antialias -stroke grey -fill white -annotate +0+0 "$(echo "${WTI}\n${FORTUNE}" | fold -w50)" -wave 1x20 bottom.png
convert +transparent white bottom.png bottom.png

