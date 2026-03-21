#!/usr/bin/python3

import feedparser
import subprocess
import datetime
import random
import sqlite3

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        create table if not exists feeds (
            url text primary key, 
            title text not null, 
            lang text not null, 
            date text not null, 
            used integer
        )
    ''')

    f = feedparser.parse("https://www.yna.co.kr/rss/news.xml")
    now = datetime.datetime.now()
    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")
    for entry in f.entries[:3]: 
        cs.execute('''
            insert or ignore into feeds 
            (url, title, lang, date, used) 
            values (?, ?, ?, ?, ?)
        ''', 
        (entry.link, entry.title, 'ko', date, 0))

    cs.execute('''
        select * from feeds 
        where used = 0 
        order by date DESC
    ''')
    feeds = cs.fetchall()
    if (len(feeds) == 0): 
        feed = f.entries[0]
        f_url = feed.link
        f_title = feed.title
        f_lang = "ko"
    else: 
        feed = feeds[0]
        f_url = feed[0]
        f_title = feed[1]
        f_lang = feed[2]
        cs.execute('''
            update feeds set used = 1 
            where url = ? 
        ''', 
        (f_url,))
    cn.commit();
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();

subprocess.run(["wkhtmltoimage", "--width", "800", "--crop-h", "800", f_url, "bot_temp.png"])
subprocess.run(["right/getfed.sh", f_url, f_title])

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
        {"nm": "MSNBC",  "url": "https://www.ms.now/rss"}
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

