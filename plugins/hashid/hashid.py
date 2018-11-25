# !hashid is used for attempting to determine the type of hash provided

import sys, string, socket, os, re
from errbot import BotPlugin, botcmd, arg_botcmd

class hashid(BotPlugin):

    @arg_botcmd('hash', type=str)  # flags a command
    def hashid(self, msg, hash=None):

      if not re.findall(r"(^[a-fA-F\d]+$)", hash):
        # Hash may contain illegal characters
        return("Your submission may contain characters not ordinarily found in hashes.  Please try again or contact the developer if you believe this to be an error.")

      dir_path = os.path.dirname(os.path.realpath(__file__))
      cmd = dir_path + "/hashidentifier.py " + hash
      output=os.popen(cmd).read()
      return(output)
