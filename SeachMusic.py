import requests
from bs4 import BeautifulSoup, Tag

from KUMusic import Music


class SearchMusic:
    music = Music()

    def search(self,keyword):
        url = "http://baidu.9ku.com/song/%s"
        payload = {}
        headers= {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        okurl = url % (keyword)
        response = requests.request("GET", okurl, headers=headers, data = payload)
        data = response.text.encode()
        soup = BeautifulSoup(data, "html5lib")

        print(soup)

        mnum = soup.select(".soAllNum")
        print(mnum)
        head = mnum[0].text
        lis:Tag = soup.select(".songList > ul:nth-child(1) li")
        print(lis)
        list = []
        for li in lis:
            id = li.input["value"][0:-1]  # 获取歌曲id
            ass = li.find_all("a")
            if(len(ass)>0):
                gqm = ass[0].text
            else:
                gqm = None
            if(len(ass)>1):
                gs = ass[1].text
            else:
                gs = None
            if(len(ass)>2):
                zj = ass[2].text
            else:
                zj = None

            list.append({
                "id":id,
                "gqm":gqm,
                "gs": gs,
                "zj": zj
            })


        # for li in select:
        #     tli:Tag = li
        #     id = tli.input["value"][0:-1] # 获取歌曲id
        #     mname = tli.a.text # 获取可取名称
        #     data = self.music.getPath(id)
        #     list.append({
        #         "id":id,
        #         "mname":mname,
        #         "mp3":data["wma"],
        #         "m4a":data["m4a"]
        #     })



        return {
            "head":head,
            "list":list
        }
