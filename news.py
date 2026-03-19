#!/usr/bin/python3

import feedparser
import datetime

dt = datetime.datetime.now()
if dt.hour > 1 and dt.hour < 15:
    try: 
	    url_hk = "https://www.newsis.com/RSS/sokbo.xml"
	    hk = feedparser.parse(url_hk)
	    for entry in hk.entries[:2]:
		    print("NEWSIS:" + entry.title)
    except Exception as e: 
	    print(e)

    try: 
	    url_am = "https://www.koreaherald.com/rss/newsAll"
	    am = feedparser.parse(url_am)
	    for entry in am.entries[:1]:
		    print("KH:" + entry.title)
    except Exception as e: 
	    print(e)
else:
    try: 
	    url_am = "https://www.newsis.com/RSS/sokbo.xml"
	    am = feedparser.parse(url_am)
	    for entry in am.entries[:2]:
		    print("NEWSIS:" + entry.title)
    except Exception as e: 
	    print(e)

    try: 
	    url_am = "https://www.vaticannews.va/en.rss.xml"
	    am = feedparser.parse(url_am)
	    for entry in am.entries[:1]:
		    print("POPE:" + entry.title)
    except Exception as e: 
	    print(e)

