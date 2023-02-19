import pymysql
import string
import random

def pick(_LENGTH):
    string_pool = string.ascii_letters + string.digits
    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)
    return result



def getcdnfile(ids):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='venex', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute(f"SELECT * FROM cdn WHERE token='"+str(ids)+"';")
    return cur.fetchone()

def addcdn(name):
    picks = pick(8)+pick(8)+pick(8)
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='venex', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute(f"INSERT INTO cdn(token, filename) VALUES('{picks}', '{name}');")
    con.commit()
    con.close()
    return f'{picks}'
