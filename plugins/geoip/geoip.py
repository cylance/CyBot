# !geoip is used for Querying the freegeoip.net API

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

class geoip(BotPlugin):

    @arg_botcmd('query', type=str)  # flags a command
    def geoip(self, msg, query=None): 
        url = query
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent" : "You all rock!"
            }
        response = requests.get('http://ip-api.com/json/' + url,
            headers=headers)

        str_resp = response.text
        str_resp = re.sub('{', '', str_resp)
        str_resp = re.sub('}', '', str_resp)
        str_resp = re.sub(',', '\r\n', str_resp)
        return(str_resp)
