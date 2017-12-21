# !bitcoin is used to query the coindesk API for the latest Bitcoin Price Index BPI

import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class bitcoin(BotPlugin):

    @botcmd # flags a command
    def bitcoin(self, msg, args):
        urlip = "https://api.coindesk.com/v1/bpi/currentprice.json"

        try:
            response = requests.get(urlip)
        except:
            return("Could not retrieve page")
            exit()

        #read html code
        data = response.json()
        return(json.dumps(data, sort_keys=True, indent=4))

