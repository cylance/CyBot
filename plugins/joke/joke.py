# !joke queryies a joke API

import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class joke(BotPlugin):

    @botcmd # flags a command
    def joke(self, msg, args):
        urlip = "https://icanhazdadjoke.com/"
        headers = {'Accept': 'application/json'}

        try:
            response = requests.get(urlip, headers=headers)
        except:
            return("Could not retrieve page")
            exit()

        #read html code
        data = response.json()
        return(data["joke"])

