# !stats is used for parsing its own logs.  The date format can be YYYY-MM or YYYY-MM-DD.

import os, requests, json, re, sys, datetime
from collections import Counter
from errbot import BotPlugin, botcmd, arg_botcmd

class stats(BotPlugin):

    @arg_botcmd('date', type=str) # flags a command
    def stats(self, msg, date=None):
        
        # Read the errbot log
        LOCATION = os.path.dirname(__file__)
        errbotlog = LOCATION + "/../../errbot.log"
		
        with open(errbotlog, "r") as file:
            lines = file.read()

        # Check date format
        matched = re.match(r'(\d{4}$)', date) or re.match(r'(\d{4}-\d{2}$)', date) or re.match(r'(\d{4}-\d{2}-\d{2}$)', date)
        if not matched:
            return("Please check your date for proper format of YYYY or YYYY-MM or YYYY-MM-DD")
            exit()

        searchstring = date + ".*Processing.*"

        # Find all of the Processing lines that match that date
        entryfound = re.findall(searchstring, lines)

        # Initialize the commandlist argument list
        commandlist=[]
        arglist=[]

        # Get the commands into a list
        for line in entryfound:
            words = line.split()
            # filter out reserved commands
            if words[6][1:-1] != "room_join" and words[6][1:-1] != "room_list" and words[6][1:-1] != "room_leave" and words[6][1:-1] != "help" and words[6][1:-1] != "restart" and words[6][1:-1] != "shutdown" and words[6][1:-1] != "stats" and words[6][1:-1] != "cc":
                commandlist.append(words[6][1:-1])
                arglist.append(words[9][1:-1].lower().replace('http', 'hxxp'))

        CommandFreq = Counter(commandlist).most_common(25)
        ArgFreq = Counter(arglist).most_common(25)

        answer = "# Number of tasks requested: " + str(len(commandlist)) + "\r\n"

        answer += "# Top 25 most frequent commands:\r\n"
        for value, count in CommandFreq:
            answer += value + " : " + str(count) + "\r\n"

        answer += "# \r\n"
        answer += "# Top 25 most frequent arguments:\r\n"
        for value, count in ArgFreq:
            answer += "'" + value + "'" + " : " + str(count) + "\r\n"

        if str(len(commandlist))=="0":
            answer = "No results found. Please check your date for proper format of YYYY or YYYY-MM or YYYY-MM-DD and ensure the date has data."

        return(answer)

