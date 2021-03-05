import json

import requests

class Music:
    url = "http://www.9ku.com/html/playjs/185/%s.js"
    payload = {}
    headers= {}

    def getPath(self,id):
        okurl = self.url % (id)
        response = requests.request("GET", okurl, headers=self.headers, data = self.payload)
        mp3data = json.loads(response.text[1:-1])
        name = mp3data["mname"]
        wma = mp3data["wma"]
        m4a = mp3data["m4a"]
        return {
            "name":name,
            "wma":wma,
            "m4a":m4a
        }
