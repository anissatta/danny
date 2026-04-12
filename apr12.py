#!/usr/bin/python3

import feedparser
import datetime
import sqlite3

now = datetime.datetime.now()
yay = [  {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/etoday_news_all.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/market_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/finance_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/land_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/industry_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/economy_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/global_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/politics_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/society_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/opinion_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/culture-life_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://rss.etoday.co.kr/eto/news-factory_news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/news.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/newsbest.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_59.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_67.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_68.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_69.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_83.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.kenews.co.kr/data/rss/section_70.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/newsflesh"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/politics"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/society"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/culture"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/sports"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/economy"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/international"},
         {"lng": "ko", "nm": "MISC", "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/entertainment"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.yonhapnewstv.co.kr/browse/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/politics/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/economy/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/society/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/local/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/culture/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/sports/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.yonhapnewstv.co.kr/category/news/weather/feed/"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/region/1"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/region/2"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/region/6"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/region/10"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/industry/1200"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/industry/1000"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/industry/1100"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/industry/100"},
         {"lng": "ko", "nm": "MISC", "url": "https://api.newswire.co.kr/rss/industry/600"},
         {"lng": "ko", "nm": "MISC","url": "http://www.newsfarm.co.kr/rss/allArticle.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/clickTop.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N33.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N34.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N36.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N68.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N72.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N73.xml"},
         {"lng": "ko", "nm": "MISC", "url": "http://www.newsfarm.co.kr/rss/S2N80.xml"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.imaeil.com/rss"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssAll"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssPublic"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssCulture"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssPolitics"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssEconomy"},
         {"lng": "ko", "nm": "MISC", "url": "https://www.jjan.kr/news/rssPeople"}]

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")

    for y in yay: 
        print("Processing: " + y["url"])
        outlet_url  = y["url"]
        outlet_name = y["nm"]
        outlet_lang = y["lng"]
        f = feedparser.parse(outlet_url)
        for entry in f.entries[:12]: 
            cs.execute('''
                insert or ignore into mixed 
                (url, title, outlet, lang, date, used) 
                values (?, ?, ?, ?, ?, ?)
            ''', 
            (entry.link, entry.title, outlet_name, outlet_lang, date, 0))
    cn.commit();
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();

