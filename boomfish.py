# from flask import Flask
from flask import *
import urllib, hashlib
import time
import sqlite3
from os import urandom, path
import json

app = Flask(__name__)
app.debug = True

app.secret_key = urandom(16)
randomkey = urandom(48)

if path.exists('/boomfish/db/test.db'):
    DATABASE_URL = '/boomfish/db/test.db'
else:
    DATABASE_URL = 'test.db'
# DATABASE_URL=':memory:'

admin_username = 'hcreak'
admin_password = 'kotori'


def gravatar_url(email):
    # gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url = "https://secure.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'s': str(32), 'r': 'X', 'd': 'identicon'})
    return gravatar_url


def checkkey():
    key = session.get('key')
    if key == None:
        return False
    if key == randomkey:
        return True
    else:
        return False


# old getdata (ALL)
# def getdata():
#     conn = sqlite3.connect(DATABASE_URL)
#     cur = conn.execute("SELECT * FROM data;")
#     conn.commit()
#
#     itemlist = [{'id': item[0],
#                  'author': item[1],
#                  'gravatar': item[2],
#                  'time': str(item[3]),
#                  'strtime': str(time.strftime("%B %d, %Y at %H:%M", time.localtime(item[3]))),
#                  'text': item[4],
#                  'weburl': item[5]} for item in cur.fetchall()]
#     # email = ''
#     # gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
#     # gravatar_url += urllib.urlencode({'s': str(32), 'r': 'X', 'd': 'identicon'})
#
#     # item = {}
#     # item['author'] = 'q'
#     # item['gravatar'] = gravatar_url
#     # item['time'] = str(time.time())
#     # item['strtime'] = str(time.strftime("%B %d, %Y at %H:%M", time.localtime()))
#     # item['text'] = 'fuck!'
#     # item['weburl'] = 'http://yyq.cn'
#     # itemlist = []
#     # itemlist.append(item)
#     # itemlist.append(item)
#     # itemlist.append(item)
#
#     mode = None
#     if checkkey():
#         mode = 'admin'
#     return render_template("insert.html",itemlist=itemlist, mode=mode, admin_username=admin_username)

def getdata(datanum):
    execstr = "SELECT * FROM data WHERE " + (' or '.join('id=' + str(i) for i in datanum)) + ";"
    conn = sqlite3.connect(DATABASE_URL)
    cur = conn.execute(execstr)
    conn.commit()

    itemlist = [{'id': item[0],
                 'author': item[1],
                 'gravatar': item[2],
                 'time': str(item[3]),
                 'strtime': str(time.strftime("%B %d, %Y at %H:%M", time.localtime(item[3]))),
                 'text': item[4],
                 'weburl': item[5]} for item in cur.fetchall()]

    mode = None
    if checkkey():
        mode = 'admin'
    return render_template("insert.html", itemlist=itemlist, mode=mode, admin_username=admin_username)


@app.route('/', methods=['GET'])
def test():
    return render_template("index.html")


@app.route('/comment', methods=['POST'])
def add():
    conn = sqlite3.connect(DATABASE_URL)
    conn.execute(
        'INSERT INTO data (author,gravatar,time,text,weburl) VALUES (?,?,?,?,?)',
        [request.form['author'],
         gravatar_url(request.form['mail']),
         time.time(),
         request.form['text'],
         request.form['url']]
    )
    conn.commit()
    return redirect('/')


@app.route('/bug', methods=['GET', 'POST'])
def bug():
    if request.method == 'POST':
        if request.form['username'] == hashlib.md5(admin_username).hexdigest() \
                and request.form['password'] == hashlib.md5(admin_password).hexdigest():
            session['key'] = randomkey
            return redirect('/')
        else:
            return redirect('/bug')

    if request.method == 'GET':
        if not session.get('key'):
            return render_template("login.html")
        else:
            session.clear()
            return redirect('/')


@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    if checkkey():
        conn = sqlite3.connect(DATABASE_URL)
        conn.execute('DELETE FROM data WHERE id = ?', [id])
        conn.commit()
        return redirect('/')
    else:
        return redirect('/bug')


@app.route('/refurbish', methods=['POST'])
def refurbish():
    data = json.loads(request.form['data'])
    blist = [int(i) for i in data]

    conn = sqlite3.connect(DATABASE_URL)
    cur = conn.execute("SELECT id FROM data;")
    conn.commit()
    alist = [i[0] for i in cur.fetchall()]

    delnums = list(set(blist).difference(set(alist)))  # blist V alist X --> send del
    addnums = list(set(alist).difference(set(blist)))  # alist V blist X --> send add

    if len(addnums) != 0:
        return getdata(addnums)
    else:
        return 'Norefurbish'


if __name__ == '__main__':
    app.run()
