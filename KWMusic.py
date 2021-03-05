import json

import requests


class KWMusic:
    url = "http://www.kuwo.cn/url?format=mp3&rid=%s&response=url&type=convert_url3&br=512kmp3&from=web"
    payload = {}
    headers= {}

    def getPath(self,id):
        okurl = self.url %(id)
        payload = {}
        headers = {}
        response = requests.request("GET",okurl, headers=headers, data=payload)
        loads = json.loads(response.text)
        return {
            "name":None,
            "wma":loads["url"],
            "m4a":None
        }




