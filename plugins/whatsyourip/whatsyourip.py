# !whatsyourip queries ipinfo.io/ip for IP information

import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class whatsyourip(BotPlugin):

    @botcmd # flags a command
    def whatsyourip(self, msg, args):
        urlip = "http://ipinfo.io/ip"
        headers = {'Accept': 'application/json'}

        try:
            response = requests.get(urlip, headers=headers)
        except:
            return("Could not retrieve page")
            exit()

        #read html code
        return(response.text)

