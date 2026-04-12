#!/usr/bin/python3

import subprocess
import sqlite3
import datetime

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select substring(date, 12, 4), yna, newsis, hbiz from stat2 
        order by date ASC 
    ''')
    rs = cs.fetchall()

    for r in rs: 
        print("\"" + r[0] + "\" " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]))

    # clean up. 
    now = datetime.datetime.now()
    old = now + datetime.timedelta(minutes=-120)
    cs.execute('''
        delete from stat2 
        where date < ? 
    ''', (old.strftime("%Y-%m-%d-%H%M"),))
    cn.commit()

except Exception as e: 
    print(e)
finally: 
    cn.close();

