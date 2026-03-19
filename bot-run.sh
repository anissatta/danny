#!/bin/sh

i=85

while true
do
    ./bot.py
    ./bot-optional.sh $i
    ./kamsys-ng.sh

    i=$(($i+1))
    sleep 240
done

