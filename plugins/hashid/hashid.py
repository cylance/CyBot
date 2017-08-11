# !hashid is used for attempting to determine the type of hash provided

import sys, string, socket, os
from errbot import BotPlugin, botcmd, arg_botcmd

class hashid(BotPlugin):

    @arg_botcmd('hash', type=str)  # flags a command
    def hashid(self, msg, hash=None):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cmd = dir_path + "/hashidentifier.py " + hash
        output=os.popen(cmd).read()
        return(output)
