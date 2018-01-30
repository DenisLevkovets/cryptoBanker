import sqlite3
import sys
import pymysql


DB_HOST = "92.53.67.130"
DB_USER = "remote"
DB_PASSWORD = "conass"
DB_NAME = "crypt"


if sys.platform == 'win32' and False:
    #print('lll')
    paramstyle = '?'
else:
    paramstyle = "%s"


def connect():
    if sys.platform == 'win32' and False:
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


def get_text(uid, t_type):
    lang = execute('SELECT lang FROM users WHERE uid = %(p)s', uid)
    db = connect()
    cur = db.cursor()
    cur.execute(f'SELECT {t_type} FROM texts WHERE lang = %s', lang)
    text = cur.fetchone()
    db.close()
    return text


def create_user(cid, lang):
    if execute("SELECT * FROM users WHERE cid=%(p)s", cid):
        return 0
    execute('INSERT INTO users (uid, lang) VALUES (%(p)s, %(p)s)', cid, lang, commit=True)
    # if username is None:
    #     execute("INSERT INTO users(cid, name) VALUES (%(p)s, %(p)s)", cid, name, commit=True)
    # else:
    #     execute("INSERT INTO users(cid, name, username) VALUES (%(p)s, %(p)s, %(p)s)", cid, name, username, commit=True)
    return 1
