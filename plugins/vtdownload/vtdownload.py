# !vtdownload - Plugin to download malware sample provided a given hash

import datetime, os, requests, re, pyminizip
from errbot import BotPlugin, botcmd, arg_botcmd

apikey=""

class vtdownload(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def vtdownload(self, msg, args):

        # Test for at least 1 argument
        if len(args) != 1:
            return("This plugin requires a hash (MD5, SHA1, or SHA256) to download a malware sample from VirusTotal.")

        if apikey=="":
            return("This plugin requires you to enter a private VirusTotal API Key.")

        # Ensure that the hash is MD5, SHA1, or SHA256
        file_hash=args[0]
        if not (re.findall(r"(^[a-fA-F\d]{32}$)", file_hash) or re.findall(r"(^[a-fA-F\d]{40}$)", file_hash) or re.findall(r"(^[a-fA-F\d]{64}$)", file_hash)):
            # print("false")
            if not (len(file_hash)==32 or len(file_hash)==40 or len(file_hash)==64):
                return("MD5 hashes are 32, SHA1 hashes are 40, and SHA256 hashes are 64 characters in length.  Your submission is " + str(len(file_hash)) + " characters.  Please try again.")
            else:
                return("You have the right number of characters (32, 40, or 64) (Your hash length is: " + str(len(file_hash)) + "), but one of your characters is not a valid hash character of:  a-f, A-F, 0-9.")

        # Construct URL to fetch the file
        url = "https://www.virustotal.com/vtapi/v2/file/download?apikey=" + apikey + "&hash=" + file_hash

        # Define paths and variables
        fullPath = "/tmp/" + file_hash
        zipPath = fullPath + ".zi_"
        outputName = file_hash + ".zi_"
        answer = "Fetching file: " + file_hash

        try:
        # Fetch the file
            response = requests.get(url)

            # Check to see if VT has the file
            if response.status_code == 200:
                answer = answer + "\r\nReceived HTTP 200.  VirusTotal has the file!\r\n"
                with open(fullPath, 'wb') as f:
                    f.write(response.content)

                # zip with password of infected, rename as hash.zi_
                answer = answer + "Zipping the file with a password of: infected\r\n"
                pyminizip.compress(fullPath, "", zipPath, "infected", 1)

                # Send file to user via chat program
                answer = answer + "Sending file via direct message with an extension of .zi_\r\n"
                
                # Determine the sender
                channelPerson=msg.frm
                requestor = re.sub(r'#.*/', '@', str(channelPerson))
                req_id=self.build_identifier(requestor)

                stream = self.send_stream_request(req_id, open(zipPath, 'rb'), name=outputName)

                # clean up temp file
                deleteFile = "rm -f " + fullPath
                os.system(deleteFile)
                deleteFile = "rm -f " + outputName
                os.system(deleteFile)

                return(answer)

            elif response.status_code == 404:
                return("HTTP 404 received - Check the hash to ensure it is correct and that VT has the file")
            elif response.status_code == 403:
                return("HTTP 403 received - Check your API key to ensure it is a private key with access to download files")
            else:
                return("Did Not Receive an HTTP 200, 404, or 403... Do you have Internet connectivity?")

        except:
            return("Something went wrong.  Do you have pyminizip installed?  Did you enter an API Key?")
            exit()
