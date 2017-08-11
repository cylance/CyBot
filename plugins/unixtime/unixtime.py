# !unixtime is used for converting a unix timestamp to a human readable format

import datetime
from errbot import BotPlugin, botcmd, arg_botcmd

class unixtime(BotPlugin):

    @arg_botcmd('epoch', type=float)  # flags a command
    def unixtime(self, msg, epoch=None):
        return datetime.datetime.fromtimestamp(epoch).strftime('%a %Y-%m-%d %H:%M:%S')
