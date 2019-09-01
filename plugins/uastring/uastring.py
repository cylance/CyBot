# !uastring parses a user agent string and performs a lookup to determine OS and browser.

import os, requests, json, urllib.parse
from errbot import BotPlugin, botcmd, arg_botcmd

class uastring(BotPlugin):

    @arg_botcmd('uastring', type=str)  # flags a command
    def uastring(self, msg, uastring=None):

        raw_param = { 'uas' : uastring}
        encoded_param=urllib.parse.urlencode(raw_param)
        urlip = "http://www.useragentstring.com/?getJSON=all&" + encoded_param

        try:
            response = requests.get(urlip)
        except:
            return("Could not retrieve page")
            exit()

        #read html code
        data = response.json()
        answer = "Answer (Non-empty fields): \r\n"
        for key, value in data.items():
          if value!="":
              answer+= str(key) + ": " + str(value) + "\r\n"
        return(answer)
