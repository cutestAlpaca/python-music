import eyed3
import requests

from KWMusic import KWMusic
from SeachKWMusic import SearchKWMusic


search = SearchKWMusic().search("凤凰传奇",1,50)
mlist = search["list"]
kw = KWMusic()
path = "C:/Users/48987/Desktop/凤凰传奇-50首/"


def updatempetag(url):
    audiofile = eyed3.load(opath)
    audiofile.initTag()
    audiofile.tag.artist = u"更多音乐下载"
    audiofile.tag.album = u"更多音乐下载"
    audiofile.tag.album_artist = u"更多音乐下载"
    audiofile.tag.title = u"更多音乐下载"
    audiofile.tag.save()


for m in mlist:
    try:
        pathd = kw.getPath(m["id"])
        # 歌曲名
        gqm = m["gqm"]
        # 歌手
        gs = m["gs"]
        # mp3链接
        wma = pathd["wma"]
        request = requests.request("GET", wma)
        opath = path+ gqm+"-"+gs+".mp3"
        with open(opath, 'wb')as fp:
                fp.write(request.content)
                fp.close()
        # updatempetag(opath)
        print("下载完毕",gqm+"-"+gs)
    except:
        print("错误")

