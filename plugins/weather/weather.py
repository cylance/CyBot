# !weather is used for Querying the weather in a specified zip code

import os, requests, re
from errbot import BotPlugin, botcmd, arg_botcmd

class weather(BotPlugin):

    @arg_botcmd('zipcode', type=str) # flags a command
    def weather(self, msg, zipcode=None):
        urlip = "http://api.wunderground.com/api/<APIKEY>/forecast/q/" + zipcode + ".json"

        try:
            website = requests.get(urlip)

            #read html code
            html = website.text
            
            #use re.findall to get all the lines we want
            lines = re.findall('("(title|fcttext|fcttext_metric)":".*?")', html)

            answer="Forecast:"

            for line in lines:
                #print(line[0])
                if "title" in line[0]:
                    answer = answer + "\r\n"
                answer = answer + "\r\n" + line[0].split(":")[1]

            return(answer)

        except:
            return("Could not retrieve weather")
            exit()
