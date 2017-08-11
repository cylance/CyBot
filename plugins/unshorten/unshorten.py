# !unshorten is used for unshortening a URL

import os, requests, string, re
from errbot import BotPlugin, botcmd, arg_botcmd

class Unshorten(BotPlugin):

    @arg_botcmd('url', type=str)  # flags a command
    def unshorten(self, msg, url=None):
        try:
            headers = {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "none",
                "Accept-Language": "en-US,en;q=0.8",
                "Connection": "keep-alive"
                }
            response = requests.get('https://unshorten.me/raw/' + url, headers=headers)
            data = response.text
            data = re.sub('http', 'hxxp', data)
            return(data)
        except:
            data =  'Apologies, but an error occurred.'
            return data 
