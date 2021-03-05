from flask import Flask, request, render_template

from KWMusic import KWMusic
from SeachKWMusic import SearchKWMusic
app = Flask(__name__)


@app.route('/findmusic',methods=["POST"])
def findmusic():
    keyword = request.form.get("keyword")
    page = request.form.get("page")
    pagesize = request.form.get("pagesize")
    if keyword != None:
        music = SearchKWMusic()
        search = music.search(keyword,page,pagesize)
        return search

    return {"msg":"缺少关键字"}


@app.route('/musicdetails',methods=["POST"])
def musicdetails():
    id = request.form.get("id")
    path = KWMusic().getPath(id)
    return path


@app.route('/',methods=["GET"])
def index():
    return app.send_static_file('index.html')


@app.route('/play',methods=["GET"])
def play():
    src = request.args.get("src")
    name = request.args.get("name")
    return render_template("index.html",src=src,name=name)

@app.route('/p',methods=["GET"])
def play_qq():
    id = request.args.get("id")
    data = KWMusic().getPath(id)
    return  render_template("play.html",data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6688)