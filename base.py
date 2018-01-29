import sqlite3
import sys
import pymysql


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "conass"
DB_NAME = "eth"


if sys.platform == 'win32':
    #print('lll')
    paramstyle = '?'
else:
    paramstyle = "%s"


def connect():
    if sys.platform == 'win32':
        return sqlite3.connect("db.sqlite")
    return pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, use_unicode=True, charset="utf8")


def execute(sql, *args, commit=False):
    db = connect()
    cur = db.cursor()
    cur.execute(sql % {"p": paramstyle}, args)
    if commit:
        db.commit()
        db.close()
    else:
        ans = cur.fetchall()
        db.close()
        return ans


def create_user(cid, name, username):
    if execute("SELECT * FROM users WHERE cid=%(p)s", cid):
        return 0
    if username is None:
        execute("INSERT INTO users(cid, name) VALUES (%(p)s, %(p)s)", cid, name, commit=True)
    else:
        execute("INSERT INTO users(cid, name, username) VALUES (%(p)s, %(p)s, %(p)s)", cid, name, username, commit=True)
    return 1
