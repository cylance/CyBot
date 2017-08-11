# !whois is used for Querying hackertarget's WHOIS API

import os, requests, string, re
from errbot import BotPlugin, botcmd, arg_botcmd

class whois(BotPlugin):

    @arg_botcmd('domain', type=str)  # flags a command
    def whois(self, msg, domain=None):
        try:
            params = {'q': domain}
            headers = {
                "Host": "api.hackertarget.com"
                }
            response = requests.get('https://api.hackertarget.com/whois/?q=' + domain,
                params=params, headers=headers)
            data = response.text
            data = re.sub('http', 'hxxp', data)
            return(data)
        except:
            data =  'Apologies, but an error occurred.'
            return data
