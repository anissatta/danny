#!/usr/bin/python3

import sqlite3
import random
import subprocess

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select url, title from mixed 
        where lang = 'ko' and used = 1 
        order by date DESC 
        limit 21
    ''')
    karts = cs.fetchall()
    kart = karts[random.randint(0, len(karts)-1)]
    url = kart[0]
    title = kart[1]

    ret = subprocess.run(["trans", "-b", "ko:en", title], capture_output=True, text=True)
    translated = ret.stdout

    print(title.rstrip("\n"))
    print(translated.rstrip("\n"))
    print(url.rstrip("\n"))

except Exception as e: 
    print(e)
finally: 
    cn.close();

