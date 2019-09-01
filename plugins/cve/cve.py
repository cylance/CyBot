# !cve queries the CIRCL CVE database

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

class cve(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def cve(self, mess, args):

        if len(args)!=1:
            return("Incorrect number of parameters.  Must either specifcy the CVE number ####-#### or a digit # for the most recent N CVE's")
            exit()

        # Assign arguments to variables
        arg=args[0]
        if re.match(r'^[\d]{4}\-[\d]{4}$', arg):
          url = "http://cve.circl.lu/api/cve/CVE-" + arg
          try:
              response = requests.get(url)
          except:
              return("Could not retrieve page")
              exit()
        elif re.match(r'^[\d]+$', arg):
          url = "http://cve.circl.lu/api/last/" + arg
          try:
              response = requests.get(url)
          except:
              return("Could not retrieve page")
              exit()
        else:
          return("Error: Input must be an integer or a CVE number in the format: ####-####.")

        data_list = response.json()
        answer = ""
        #iterate over a list of dict entries
        for json_entry in data_list:
            answer+="##ID:  " + str(json_entry["id"]) + "\r\n"
            answer+="Summary:  " + str(json_entry["summary"]) + "\r\n"
            answer+="Published:  " + str(json_entry["Published"]) + "\r\n"
            answer+="Last Modifiedd:  " + str(json_entry["last-modified"]) + "\r\n"
            answer+="CVSS:  " + str(json_entry["cvss"]) + "\r\n"
            answer+="References:  " + str(json_entry["references"]) + "\r\n\r\n"

        return(answer)
