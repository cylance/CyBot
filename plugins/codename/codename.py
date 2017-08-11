# !codename is used to query and extract a codename from Mark Biek's site

import string, urllib, re
from errbot import BotPlugin, botcmd, arg_botcmd

class codename(BotPlugin):

    @botcmd # flags a command
    def codename(self, msg, args):
        urlip = "https://mark.biek.org/code-name/"

        try:
            website = urllib.request.urlopen(urlip)
        except:
            return("Could not retrieve page")
            exit()

        #read html code
        html = website.read().decode('utf-8')

        #use re.search to find the codename
        codename = re.search(r'<h1>(.*?)<\/h1>', html).group(1)

        return codename

