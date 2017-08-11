# !linkextractor is used for extracting links from sites

import requests, re
from errbot import BotPlugin, botcmd, arg_botcmd

class linkextractor(BotPlugin):

    @arg_botcmd('urlip', type=str)  # flags a command
    def linkextractor(self, msg, urlip=None):
        try:
            website = requests.get(urlip)
            
            #read html code
            html = website.text

            #use re.findall to get all the links
            links = re.findall('"((http|ftp)s?://.*?)"', html)

            answer="Links extracted from the page:"

            for link in links:
                #print(link[0])
                answer = answer + "\r\n" + re.sub('http', 'hxxp', link[0])

            return(answer)

        except:
            return("Could not retrieve page")
            exit()



