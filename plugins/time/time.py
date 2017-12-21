# !time is used for Querying an API that returns the current time in a specified timezone

import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class time(BotPlugin):

    @arg_botcmd('tz', type=str) # flags a command
    def time(self, msg, tz=None):
        urlip = "http://worldclockapi.com/api/json/" + tz + "/now"

        try:
            response = requests.get(urlip)
        except:
            return("Error:  Could not retrieve time")
            exit()

        #read html code
        data = response.json()
        return(json.dumps(data, sort_keys=True, indent=4))

