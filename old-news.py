#!/usr/bin/python3

import feedparser
import datetime
import random

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

    mynews = [
        "Dear disturbers: I'll detect you & you'll be miserably wiped out.",
        "Yukiko, my stepmom, has ADHD & her two sons also have it.",
        "I have a notebook with the names of wannabes written on it. I've perceived that 'wannabes' wanted to be something.",
        "Recently I left the hospital at which a disturber tried to toy my project along with my finger.",
        "Peace on earth is important but to me what matters the most is my relationship with Ms. L. My parents may ruined the latter so they shall ruin the former, too.",
        "I was treated as an ADHD person at KIX3 thanks to some rumor. And this rumor may affected the Itaewon tragedy. So..."
    ]
    print(mynews[random.randint(0, len(mynews)-1)])

