# !vtquery is used for Querying the VirusTotal API

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

apikey = "changeme"

class VTQuery(BotPlugin):

    @arg_botcmd('query', type=str)  # flags a command
    def vt(self, msg, query=None):
	
	    # Check to make sure VT API key was entered
        if apikey=="changeme":
            return("Error:  A Public or private VirusTotal API Key was not configured in the plugin.  This function will not work until this is fixed.")

        # Determine if it was a hash or URL submitted
        if (re.findall(r"(^[a-fA-F\d]{32}$)", query) or re.findall(r"(^[a-fA-F\d]{40}$)", query) or re.findall(r"(^[a-fA-F\d]{64}$)", query)):

            #It was a hash
            params = {'apikey': apikey, 'resource': query}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "Thank you"
                }
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                params=params, headers=headers)

            resp = response.json()
            # If VirusTotal does not have results, display the error message.
            if resp['response_code']==0:
                return(str(resp['verbose_msg']))

            answer = "Hits: " + str(resp['positives']) + " / " + str(resp['total']) + "\r\n"
            answer += "Scan Date: " + str(resp['scan_date']) + "\r\n"
            answer += "MD5: " + str(resp['md5']) + "\r\n"
            answer += "SHA1: " + str(resp['sha1']) + "\r\n"
            answer += "SHA256: " + str(resp['sha256']) + "\r\n"
            answer += "Link to Results: " + str(resp['permalink']) + "\r\n"
            answer += "Hits:\r\n"
            if str(resp['positives'])=="0":
                answer += "None\r\n"
            else:
                for n in resp['scans']:
                    if str(resp['scans'][n]['detected'])=="True":
                        answer += n + ": " + str(resp['scans'][n]['result']) + "    (Version: " +  str(resp['scans'][n]['version']) + "    Updated: " +  str(resp['scans'][n]['update']) + ")\r\n"
            return(answer)

        else:
            # It was a URL
            url = query
            # Remove the defanging of the URL to submit
            url = re.sub('[\[()\]]', '', url)
            params = {'apikey': apikey, 'resource': url}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  My Python requests library example client or username"
                }
            response = requests.get('https://www.virustotal.com/vtapi/v2/url/report',
                params=params, headers=headers)

            resp = response.json()

            # If VirusTotal does not have results, display the error message.
            if resp['response_code']==0:
                return(str(resp['verbose_msg']))
				
            answer = "Hits: " + str(resp['positives']) + " / " + str(resp['total']) + "\r\n"
            answer += "Scan Date: " + str(resp['scan_date']) + "\r\n"
            answer += "URL: " + str(resp['url']) + "\r\n"
            answer += "Link to Results: " + str(resp['permalink']) + "\r\n"
            answer += "Hits:\r\n"
            if str(resp['positives'])=="0":
                answer += "None\r\n"
            else:
                for n in resp['scans']:
                    if str(resp['scans'][n]['detected'])=="True":
                        answer += n + ": " + str(resp['scans'][n]['result'])
                        if 'detail' in resp['scans'][n]:
                            answer += "    Link: " + str(resp['scans'][n]['detail']) + "\r\n"
                        else:
                            answer += "\r\n"
            return(answer)
