import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content, imsas):
    con = sql.connect(path.join(ROOT, 'databs.db'))
    cur = con.cursor()
    cur.execute('insert into posts (nombre, content, imaag) values (?,?,?)', (name, content, imsas))
    con.commit()
    con.close()
    get_por(name, content)

def create_table():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    sqla = "create table posts (id integer primary key autoincrement, nombre text not null, content text not null, imaag blob not null)"
    cur.execute(sqla)
    con.commit()
    con.close()
    
def get_post():
    con = sql.connect(path.join(ROOT, 'databs.db'))
    cur = con.cursor()
    cur.execute('select * from posts ORDER BY id ASC')
    posts = cur.fetchall()
    return posts

def get_por(nomb, content):
    con = sql.connect(path.join(ROOT, 'databs.db'))
    cur = con.cursor()
    cur.execute('select * from posts where nombre= ?', (nomb,))
    posts = cur.fetchall()
    sad(posts, nomb, content)
    con.close()

def sad(pos, nomb, content):
    for u in pos:
        with open(f'static/upload/{nomb}.{content}', 'wb') as f:
            f.write(u[-1])