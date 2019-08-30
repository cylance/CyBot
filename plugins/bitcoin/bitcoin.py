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
        results = "Updated:  " + str(data["time"]["updated"]) + "\r\n"
        results += "USD:  " + str(data["bpi"]["USD"]["rate"]) + "\r\n"
        results += "GBP:  " + str(data["bpi"]["GBP"]["rate"]) + "\r\n"
        results += "EUR:  " + str(data["bpi"]["EUR"]["rate"]) + "\r\n"
        results += "Disclaimer:  " + str(data["disclaimer"]) + "\r\n"

        return(results)
