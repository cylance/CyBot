# !screenshot is used for grabbing a screenshot of a website without visiting it directly

import datetime, os, requests, re
from errbot import BotPlugin, botcmd, arg_botcmd

class screenshot(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def screenshot(self, msg, args):


        # Test for at least 1 argument
        if len(args) != 1:
            return("This plugin requires only one argument of a full URL to include protocol. Defanged URLS accepted [] or ().")

        url=args[0]

        #strip defanging brackets and parenthesis
        url = re.sub('[\[()\]]', '', url)

        #validate URL
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(regex, url):
            return("This plugin requires only one argument of a full URL to include protocol. Defanged URLS accepted [] or ().")


        # Construct URL to fetch the image
        urlip = "http://image.thum.io/get/" + url

        try:

            tempfile = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
            fullPath = "/tmp/" + tempfile
            outputName=urlip + ".png"

            # Fetch the image
            response = requests.get(urlip)
            if response.status_code == 200:
                with open(fullPath, 'wb') as f:
                    f.write(response.content)

            stream = self.send_stream_request(msg.frm, open(fullPath, 'rb'), name=outputName)

            #clean up temp file
            deleteFile = "rm -f " + fullPath
            os.system(deleteFile)

            return("Image Fetched!")

        except:
            return("Could not retrieve the site")
            exit()
