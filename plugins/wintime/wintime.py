# !wintime is used for converting a Windows timestamp to a human readable format

import time, datetime
from errbot import BotPlugin, botcmd, arg_botcmd

class wintime(BotPlugin):

    @arg_botcmd('epoch', type=float)  # flags a command
    def wintime(self, msg, epoch=None):
        d=11644473600 #difference between 1601 and 1970
        unixtime = (epoch/10000000) - d
        return datetime.datetime.fromtimestamp(unixtime).strftime('%a %Y-%m-%d %H:%M:%S')
