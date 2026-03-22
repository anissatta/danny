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

# top  
outlets = [
    {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/sokbo.xml"},
    {"lng": "ko", "nm": "CHOSUN1","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/international/?outputType=xml"},
    {"lng": "ko", "nm": "CHOSUN2","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/culture-life/?outputType=xml"},
    {"lng": "ko", "nm": "MK",     "url": "https://www.mk.co.kr/rss/40300001/"},
    {"lng": "ko", "nm": "HK",     "url": "https://www.hankyung.com/feed/all-news"},
    {"lng": "ko", "nm": "HBIZ",   "url": "https://biz.heraldcorp.com/rss/google/newsAll"},
    {"lng": "ko", "nm": "KPOP",   "url": "https://www.heraldmuse.com/rss/google/hm_kpop"},
    {"lng": "en", "nm": "PBS",    "url": "https://www.pbs.org/newshour/feeds/rss/headlines"},
    {"lng": "en", "nm": "SDOT",   "url": "https://rss.slashdot.org/Slashdot/slashdotMain"},
    {"lng": "en", "nm": "NYT",    "url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"},
    {"lng": "en", "nm": "GDN1",   "url": "https://www.theguardian.com/us-news/us-politics/rss"},
    {"lng": "en", "nm": "GDN2",   "url": "https://www.theguardian.com/world/middleeast/rss"},
    {"lng": "en", "nm": "GDN3",   "url": "https://www.theguardian.com/world/rss"},
    {"lng": "en", "nm": "GDNC",   "url": "https://www.theguardian.com/uk/commentisfree/rss"},
    {"lng": "en", "nm": "HILL",   "url": "https://thehill.com/feed/"},
    {"lng": "en", "nm": "MSNBC",  "url": "https://www.ms.now/rss"},
    {"lng": "en", "nm": "FOX",    "url": "https://moxie.foxnews.com/google-publisher/latest.xml"},
    {"lng": "en", "nm": "FP",     "url": "https://foreignpolicy.com/rss"},
    {"lng": "en", "nm": "ET",     "url": "https://www.etonline.com/news/rss"},
    {"lng": "en", "nm": "CGTN",   "url": "https://www.cgtn.com/subscribe/rss/section/world.xml"},
    {"lng": "en", "nm": "NDTV",   "url": "https://feeds.feedburner.com/ndtvnews-latest"},
    {"lng": "hi", "nm": "DB",     "url": "https://www.bhaskar.com/rss-v1--category-4587.xml"},
    {"lng": "ja", "nm": "ASAHI",  "url": "https://www.asahi.com/rss/asahi/newsheadlines.rdf"},
    {"lng": "ja", "nm": "NIKKEI", "url": "https://business.nikkei.com/rss/sns/nb.rdf"}
]

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        create table if not exists mixed (
            url text primary key, 
            title text not null, 
            outlet text not null, 
            lang text not null, 
            date text not null, 
            used integer
        )
    ''')

    i = random.randint(0, len(outlets)-1)
    outlet_url = outlets[i]["url"]
    outlet_name = outlets[i]["nm"]
    outlet_lang = outlets[i]["lng"]
    f = feedparser.parse(outlet_url)
    now = datetime.datetime.now()
    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")
    for entry in f.entries[:3]: 
        cs.execute('''
            insert or ignore into mixed 
            (url, title, outlet, lang, date, used) 
            values (?, ?, ?, ?, ?, ?)
        ''', 
        (entry.link, entry.title, outlet_name, outlet_lang, date, 0))

    cs.execute('''
        select * from mixed 
        where used = 0 
        order by date DESC
    ''')
    feeds = cs.fetchall()
    if (len(feeds) == 0): 
        feed = f.entries[0]
        f_url = feed.link
        f_title = feed.title
        f_outlet = outlet_name
        f_lang = outlet_lang
    else: 
        feed = feeds[0]
        f_url = feed[0]
        f_title = feed[1]
        f_outlet = feed[2]
        f_lang = feed[3]
        cs.execute('''
            update mixed set used = 1 
            where url = ? 
        ''', 
        (f_url,))

    subprocess.run(["top/getfed.sh", f_outlet, f_url, f_title, f_lang])

    cn.commit();
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();

try: 
    url_am = "https://mycatiskorean.blogspot.com//feeds/posts/default"
    am = feedparser.parse(url_am)
    url_art = am.entries[0].link
    subprocess.run(["wkhtmltoimage", "--width", "320", "--crop-y", "321", "--crop-h", "480", url_art, "fright.png"])
except Exception as e: 
    print(e)

