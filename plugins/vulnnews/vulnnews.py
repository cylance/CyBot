# !vulnnews is used for qurying Google News for CVE Vulnerability

import requests, re
import xml.etree.ElementTree as ET
from errbot import BotPlugin, botcmd, arg_botcmd

class vulnnews(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def vulnnews(self, msg, args):

        #Define default number of articles
        limit=10
        urlip = "https://news.google.com/news/rss/search/section/q/CVE%20vulnerability/CVE%20vulnerability?hl=en&gl=US&ned=us"

        print(len(args))
        if len(args)!=1 and len(args)!=0:
            return("Incorrect number of parameters.  Can either be 0 or 1 arguments.")
            exit()

        if len(args)==1:
            if args[0].isdigit():
                limit=int(args[0])
            else:
                return("Only acceptable argument is a number to specify the article count.")
                exit()

        try:
            website = requests.get(urlip)

            #read html code
            html = website.text.encode('utf-8')

            root = ET.fromstring(html)

            count = 1
            answer = "Your news:"

            for item in root.iter('item'):
                title = item.find('title').text
                link = item.find('link').text
                answer += "\r\n"
                answer += str(count) + ") " + title
                answer += "\r\n"
                answer += link
                count += 1
                if count>limit:
                    break

            return(answer)
        except:
            return("Could not retrieve page")
            exit()
