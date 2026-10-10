import sqlite3

try:
    conn = sqlite3.connect("C:\training\day-1\day5\\prod.db")
except Exception as eobj:
    print("DB Connection failed."+str(eobj))

sth = conn.cursor()
sth.execute("select *from prod")
for var in sth:
    print(var)
conn.close()
