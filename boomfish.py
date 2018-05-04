# from flask import Flask
from flask import *
import urllib, hashlib
import time
import sqlite3

app = Flask(__name__)
app.debug = True
DATABASE_URL = 'test.db'
# DATABASE_URL=':memory:'


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

def gravatar_url(email):
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'s': str(32), 'r': 'X', 'd': 'identicon'})
    return gravatar_url


@app.route('/')
def test():
    conn = sqlite3.connect(DATABASE_URL)
    cur = conn.execute("SELECT * FROM data;")
    conn.commit()

    itemlist = [{'author': item[1],
                 'gravatar': item[2],
                 'time': str(item[3]),
                 'strtime': str(time.strftime("%B %d, %Y at %H:%M", time.localtime(item[3]))),
                 'text': item[4],
                 'weburl': item[5]} for item in cur.fetchall()]
    # email = ''
    # gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    # gravatar_url += urllib.urlencode({'s': str(32), 'r': 'X', 'd': 'identicon'})

    # item = {}
    # item['author'] = 'q'
    # item['gravatar'] = gravatar_url
    # item['time'] = str(time.time())
    # item['strtime'] = str(time.strftime("%B %d, %Y at %H:%M", time.localtime()))
    # item['text'] = 'fuck!'
    # item['weburl'] = 'http://yyq.cn'
    # itemlist = []
    # itemlist.append(item)
    # itemlist.append(item)
    # itemlist.append(item)

    sum = len(itemlist)
    return render_template("index.html", sum=sum, itemlist=itemlist)


@app.route('/comment', methods=['POST'])
def add():
    conn = sqlite3.connect(DATABASE_URL)
    cur = conn.execute(
        'INSERT INTO data (author,gravatar,time,text,weburl) VALUES (?,?,?,?,?)',
        [request.form['author'],
         gravatar_url(request.form['mail']),
         time.time(),
         request.form['text'],
         request.form['url']]
    )
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()
