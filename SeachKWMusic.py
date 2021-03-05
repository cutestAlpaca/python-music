import json

import requests
from bs4 import BeautifulSoup, Tag

from KUMusic import Music


class SearchKWMusic:

    def search(self,keyword,page,pagesize):
        url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?pn=%s&rn=%s&key=%s" %(page,pagesize,keyword)

        payload = {}
        headers = {
            'csrf': '0FRWVXK2YKZ6',
            'Referer': 'http://www.kuwo.cn/search/list?key=',
            'Cookie': 'kw_token=0FRWVXK2YKZ6',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        loads = json.loads(response.text)
        print(loads)
        list= []
        total=0
        if loads["code"]==200:
            for data in loads["data"]["list"]:

                list.append({
                    "id":data["rid"],
                    "gqm":data["name"],
                    "gs": data["artist"],
                    "zj": data["album"]
                })
            total = loads["data"]["total"]

        return {
            "head":None,
            "count":total,
            "list":list
        }
