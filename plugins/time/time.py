# !time is used for Querying an API that returns the current time in a specified timezone

import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class time(BotPlugin):

    @arg_botcmd('tz', type=str) # flags a command
    def time(self, msg, tz=None):
        urlip = "http://worldclockapi.com/api/json/" + tz + "/now"

        try:
            response = requests.get(urlip)
        except:
            return("Error:  Could not retrieve time")
            exit()

        data = response.json()
        answer = "Time Zone Name: " + str(data["timeZoneName"]) + "\r\n"
        answer += "Current Date/Time: " + str(data["currentDateTime"]) + "\r\n"
        answer += "Day of the Week: " + str(data["dayOfTheWeek"]) + "\r\n"
        answer += "Daylight Saving Time: " + str(data["isDayLightSavingsTime"]) + "\r\n"
        answer += "Ordinal Date: " + str(data["ordinalDate"]) + "\r\n"
        answer += "UTC Offset: " + str(data["utcOffset"]) + "\r\n"
        answer += "Errors: " + str(data["serviceResponse"]) + "\r\n"
        return(answer)
