# !nslookup performs a forward or reverse DNS lookup

import sys, string, socket
from errbot import BotPlugin, botcmd, arg_botcmd

class nslookup(BotPlugin):

    @arg_botcmd('question', type=str)  # flags a command
    def nslookup(self, msg, question=None):
        try:
            # Check if it is an IP address
            socket.inet_aton(question)
            ipaddr = True

        except socket.error:
            # It is probably a hostname
            ipaddr = False
        
        if ipaddr == True:
            try:
                result = socket.gethostbyaddr(question)
                result = result[0]
            except:
                result="Reverse resolution failed for: '" + question + "'" 
        else:
            try:
                result = socket.gethostbyname(question)
            except:
                result="Name resolution failed for: '" + question + "'" 

        return result 
