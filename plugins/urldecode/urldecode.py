# !urldecode is used for decoding encoded URLs

import urllib.parse, string
from errbot import BotPlugin, botcmd, arg_botcmd

class urldecode(BotPlugin):

    @arg_botcmd('url', type=str)  # flags a command
    def urldecode(self, msg, url=None):
        result=urllib.parse.unquote(url)
        return(result)
