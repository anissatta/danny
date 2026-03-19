#!/usr/bin/python3

import feedparser
import subprocess
import datetime
import random

#dt = datetime.datetime.now()
#if (dt.hour > 15 or dt.hour < 5) and dt.minute < 11: 
if False: 
    url_am = "https://trumpstruth.org/feed"
    am = feedparser.parse(url_am)
    url_art = am.entries[0].link
    subprocess.run(["wkhtmltoimage", "--width", "800", "--crop-y", "999", "--crop-h", "800", url_art, "bot_temp.png"])
else: 
    url_am = "https://www.yna.co.kr/rss/news.xml"
    am = feedparser.parse(url_am)
    url_art = am.entries[0].link
    tit_art = am.entries[0].title
    subprocess.run(["wkhtmltoimage", "--width", "800", "--crop-h", "800", url_art, "bot_temp.png"])
    subprocess.run(["right/getfed.sh", url_art, tit_art])

### NOTE: fka. top-news.py 
dt = datetime.datetime.now()
if dt.hour > 1 and dt.hour < 15: 
    # Annyeong! 
    lang="ko"
    outlets = [
        {"nm": "NEWSIS", "url": "https://www.newsis.com/RSS/sokbo.xml"},
        {"nm": "CHOSUN1","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/international/?outputType=xml"},
        {"nm": "CHOSUN2","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/culture-life/?outputType=xml"},
        {"nm": "MK",     "url": "https://www.mk.co.kr/rss/40300001/"},
        {"nm": "HK",     "url": "https://www.hankyung.com/feed/all-news"},
        {"nm": "HBIZ",   "url": "https://biz.heraldcorp.com/rss/google/newsAll"},
        {"nm": "KPOP",   "url": "https://www.heraldmuse.com/rss/google/hm_kpop"}
    ]
else: 
    # Good morning, America. 
    lang="en"
    outlets = [
        {"nm": "PBS",    "url": "https://www.pbs.org/newshour/feeds/rss/headlines"},
        {"nm": "SDOT",   "url": "https://rss.slashdot.org/Slashdot/slashdotMain"},
        {"nm": "NYT",    "url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"},
        {"nm": "GDN1",   "url": "https://www.theguardian.com/us-news/us-politics/rss"},
        {"nm": "GDN2",   "url": "https://www.theguardian.com/world/middleeast/rss"},
        {"nm": "GDN3",   "url": "https://www.theguardian.com/world/rss"},
        {"nm": "GDNC",   "url": "https://www.theguardian.com/uk/commentisfree/rss"},
        {"nm": "HILL",   "url": "https://thehill.com/feed/"},
        {"nm": "MSNBC",  "url": "https://www.ms.now/rss"},
        {"nm": "POPE",   "url": "https://www.vaticannews.va/en.rss.xml"}
    ]

try: 
    i = random.randint(0, len(outlets)-1)
    outlet_url = outlets[i]["url"]
    outlet_name = outlets[i]["nm"]
    feed = feedparser.parse(outlet_url)
    j = random.randint(0, 3)
    if j > len(feed.entries)-1: 
        j = 0
    # we'll use this one. 
    article = feed.entries[j]

    subprocess.run(["top/getfed.sh", outlet_name, article.link, article.title, lang])

except Exception as e: 
    print(e)

try: 
    url_am = "https://mycatiskorean.blogspot.com//feeds/posts/default"
    am = feedparser.parse(url_am)
    url_art = am.entries[0].link
    subprocess.run(["wkhtmltoimage", "--width", "320", "--crop-y", "321", "--crop-h", "480", url_art, "fright.png"])
except Exception as e: 
    print(e)

