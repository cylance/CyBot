# !geoip is used for Querying the freegeoip.net API

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

class geoip(BotPlugin):

    @arg_botcmd('query', type=str)  # flags a command
    def geoip(self, msg, query=None):
        #Process defanged FQDN
        query = re.sub('[\[()\]]', '', query)
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent" : "You all rock!"
            }
        response = requests.get('http://ip-api.com/json/' + query,
            headers=headers)

        json_resp = response.json()
#        print(json_resp)
        if json_resp["status"] == "success":
            answer = "Status: " + json_resp["status"] + "\r\n"
            answer += "Query: " + str(json_resp["query"]) + "\r\n"
            answer += "Org: " + str(json_resp["org"]) + "\r\n"
            answer += "ISP: " + str(json_resp["isp"]) + "\r\n"
            answer += "AS: " + str(json_resp["as"]) + "\r\n"
            answer += "Timezone: " + json_resp["timezone"] + "\r\n"
            answer += "Country: " + json_resp["country"] + "\r\n"
            answer += "Country Code: " + json_resp["countryCode"] + "\r\n"
            answer += "Region Name: " + json_resp["regionName"] + "\r\n"
            answer += "City: " + json_resp["city"] + "\r\n"
            answer += "Zip: " + json_resp["zip"] + "\r\n"
            answer += "Lat, Long: (" + str(json_resp["lat"]) + ", " + str(json_resp["lon"]) + ")\r\n"
            answer += "Best guess on a map: https://www.latlong.net/c/?lat=" + str(json_resp["lat"]) + "&long=" + str(json_resp["lon"]) + "\r\n"
        else:
            answer = "Status: " + json_resp["status"] + "\r\n"
            answer += "Message: " + json_resp["message"] + "\r\n"

        return(answer)
