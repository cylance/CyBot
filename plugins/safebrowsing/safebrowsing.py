# !safebrowsing is used for Querying the Google Safe Browsini API

import os, requests, json, re, sb
from errbot import BotPlugin, botcmd, arg_botcmd

apikey = "InsertAPIKeyHere"

class SafeBrowsing(BotPlugin):

    @arg_botcmd('query', type=str)  # flags a command
    def safebrowsing(self, msg, query=None): 
        url = query
        sbr = sb.LookupAPI(apikey) 
        resp = sbr.threat_matches_find(url) 
        return(resp) 
