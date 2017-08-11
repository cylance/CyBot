# !vtquery is used for Querying the VirusTotal API

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

apikey = "InsertAPIKeyHere"

class VTQuery(BotPlugin):

    @arg_botcmd('query', type=str)  # flags a command
    def vt(self, msg, query=None): 
        # Determine if it was a hash or URL submitted
        if (re.findall(r"(^[a-fA-F\d]{32})", query)):
            #It was a hash
            md5 = query
            params = {'apikey': apikey, 'resource': md5}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  My Python requests library example client or username"
                }
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                params=params, headers=headers)

            str_resp = response.text
            str_resp = re.sub('http', 'hxxp', str_resp)
            str_resp = re.sub('{\"scans\": {', '', str_resp)
            str_resp = re.sub('}, ', '}\n', str_resp)
            str_resp = re.sub('.*?\"detected\": false.*?[(}\n)|(}}\n)][\s]', '', str_resp)
            return(str_resp)
        else:
            # It was a URL
            url = query
            params = {'apikey': apikey, 'resource': url}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  My Python requests library example client or username"
                }
            response = requests.get('https://www.virustotal.com/vtapi/v2/url/report',
                params=params, headers=headers)

            str_resp = response.text
            str_resp = re.sub('http', 'hxxp', str_resp)
            str_resp = re.sub(', \"scans\": {', '\n', str_resp)
            str_resp = re.sub('}, ', '}\n', str_resp)
            str_resp = re.sub('.*?\"detected\": false.*[(}\n)|(}}})](\s*)', '', str_resp)
            return(str_resp)
