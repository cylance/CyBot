# !commands returns a list of possible commands

from errbot import BotPlugin, botcmd

class Commands(BotPlugin):
    @botcmd  # flags a command
    def commands(self, msg, args):
        menu = """
##== File commands ==##
 !vt <hash> - VirusTotal Query (ex: 57f222d8fbe0e290b4bf8eaa994ac641)
 !hash <hash>,<hash>,...32 max...<hash>,<hash> - Infinity API Query
 !hashid <hash> - Identify a hash type (e.g. MD5, SHA1) (Props:  c0re)

##== Network commands ==##
 !vt <URL> - VirusTotal Query
 !safebrowsing <URL> - Google Safebrowsing lookup (ex:  ihaveaproblem[.]info) (Props: Google)
 !whois <domain> - WHOIS Query (ex: cylance.com) (Props:  hackertarget.com)
 !nslookup <FQDN|IP> - DNS forward/reverse Query (ex: www.cylance.com)
 !geoip <FQDN|IP> - Perform GeoIP lookup of host (ex: www.cylance.com) (Props: freegeoip.net)
 !unshorten <shortened URL> - Unshortens URLs (ex: goo.gl/IGL1lE)
 !linkextractor <FQDN|IP> - Extracts links from a site and safely displays them (ex: hxxps://www.google.com)
 !urldecode <url> - Decodes encoded URLs (ex: /%75%72%6C?%73%61=%74)

##== Misc ==##
 !unixtime <epoch> - Convert Unix time to human readable (ex: 1347517370)
 !codename - Generates a 2 word project codename (Props: Mark Biek)
"""
        return(menu)  # This string format is markdown.
