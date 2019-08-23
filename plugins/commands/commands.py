# !commands returns a list of possible commands

from errbot import BotPlugin, botcmd

class Commands(BotPlugin):
    @botcmd  # flags a command
    def commands(self, msg, args):
        menu = """
## == File commands ==  
 !vt <hash> - VirusTotal Query (ex: 57f222d8fbe0e290b4bf8eaa994ac641)
 !vtdownload <hash> - VirusTotal Sample Download (ext: zi_, pass:infected) (ex: 57f222d8fbe0e290b4bf8eaa994ac641)
 !cuckoo -<s | u <URL> | vt <hash> | v <task_id> | r <task_id>> (ex: -vt 57f222d8fbe0e290b4bf8eaa994ac641)
 !hashid <hash> - Identify a hash type (e.g. MD5, SHA1)

## == Network commands ==
 !vt <URL> - VirusTotal Query
 !cuckoo -<s | u <URL> | vt <hash> | v <task_id> | r <task_id>> (ex: -u https://www[.]cylance[.]com)
 !safebrowsing <URL> - Google Safebrowsing lookup (ex:  ihaveaproblem[.]info)
 !whois <domain> - WHOIS Query (ex: cylance[.]com)
 !nslookup <FQDN|IP> - DNS forward/reverse Query (ex: www[.]cylance[.]com)
 !geoip <FQDN|IP> - Perform GeoIP lookup of host (ex: www[.]cylance[.]com)
 !unshorten <shortened URL> - Unshortens URLs (ex: goo[.]gl/IGL1lE)
 !screenshot <URL> - Takes a screenshot of a website and returns the .png - Accepts defanged [()] URLs
 !linkextractor <FQDN|IP> - Extracts links from a site and safely displays them (ex: https[:]//www[.]google[.]com)
 !urldecode <url> - Decodes encoded URLs (ex: /%75%72%6C?%73%61=%74)
 !uastring "<UA string>" - Enter a user Agent string in quotes to determine OS and browser (ex: Mozilla/5.0 (Windows NT 10.0; Win64; x64))

## == Threat and Vulnerability Research ==
 !ransom <search string> - Identify ransomware by searching the Ransomware Overview Spreadsheet
 !threat <search string> - Search APT group activity mapped to MITRE ATT&CK Framework
 !aptgroup <search string> - Retrieve information on common APT groups
 !hacktool <search string> - Retrieve information on common hacking tools
 !cve <#|####-####> - Return the last n CVE's or a specific ####-#### CVE
 !secnews - (Use as Private Message Only) Latest security news
 !vulnnews - (Use as Private Message Only) Latest vulnerability news

## == Misc ==
 !stats <YYYY or YYYY-MM or YYYY-MM-DD> - Produce usage statistics for a day or month (ex: 2017-12)
 !cc <Credit Card Number> - Tests validity of a CC number and attempts to determine the brand (ex: 4012888888881881 or 378282246310005)
 !time <timezone> - Query time in specified time zone (ex: utc)
 !weather <zipcode> - Query the weather in a specified zip code (ex: 21144)
 !unixtime <epoch> - Convert Unix time (seconds since Jan 1, 1970) to human readable (ex: 1347517370)
 !wintime <epoch> - Convert Windows time (100-nanosecond intervals since January 1, 1601) to human readable (ex: 131580340430000000)
 !calc <arithmetic input> - Performs basic arithmetic (Valid input: [0-9]+-*/)  (ex: 2*2*3)
 !bitcoin - Polls the latest Bitcoin Price Index
 !whatsyourip - Returns CyBot's public IP Address
 !joke - Queries an on-line API repository of jokes
 !codename - Generates a 2 word project codename

## == For issues:  Please contact Tony.Lee@Cylance.com ==
"""
        return(menu)  # This string format is markdown.
