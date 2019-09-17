# CyBot
Open Source Threat Intelligence Chat Bot

Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free and open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the home user to the largest security operations center.

We are excited to share with the world a chat bot that we affectionately call CyBot. We will show you what CyBot can do for you and graciously accept feedback on future improvements. Best of all, if you know even a little bit of Python, you can help write plugins and share them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses--quite a good return on your investment.


# CyBot Plugins

 **== File commands ==**

 !vt \<hash> - VirusTotal Query (ex: 57f222d8fbe0e290b4bf8eaa994ac641)  
 !vtdownload <hash> - VirusTotal Sample Download (ext: zi_, pass:infected) (ex: 57f222d8fbe0e290b4bf8eaa994ac641)  
 !cuckoo -<s | u <URL> | vt <hash> | v <task_id> | r <task_id>> (ex: -vt 57f222d8fbe0e290b4bf8eaa994ac641)  
 !hashid \<hash> - Identify a hash type (e.g. MD5, SHA1)  

 **== Network commands ==**

 !vt \<URL> - VirusTotal Query  
 !cuckoo -<s | u <URL> | vt <hash> | v <task_id> | r <task_id>> (ex: -vt 57f222d8fbe0e290b4bf8eaa994ac641)  
 !safebrowsing \<URL> - Google Safebrowsing lookup (ex:  ihaveaproblem[.]info)  
 !whois \<domain> - WHOIS Query (ex: cylance[.]com)   
 !nslookup \<FQDN|IP> - DNS forward/reverse Query (ex: www[.]cylance[.]com)  
 !geoip \<FQDN|IP> - Perform GeoIP lookup of host (ex: www[.]cylance[.]com)  
 !unshorten \<shortened URL> - Unshortens URLs (ex: goo[.]gl/IGL1lE)  
 !screenshot <defanged URL> - Takes a screenshot of a website and returns the .png - Accepts defanged [()] URLs  
 !linkextractor \<FQDN|IP> - Extracts links from a site and safely displays them (ex: hxxps://www[.]google[.]com)  
 !urldecode \<url> - Decodes encoded URLs (ex: /%75%72%6C?%73%61=%74)  
 !uastring \<UA String In Quotes> - Enter a user Agent string in quotes to determine OS and browser (ex: Mozilla/5.0 (Windows NT 10.0; Win64; x64))  

**== Threat and Vulnerability Research ==**

 !ransom \<search string> - Indentify ransomware by searching the Ransomware Overview Spreadsheet  
 !threat \<search string> - Search APT group activity mapped to MITRE ATT&CK Framework  
 !aptgroup \<search string> - Retrieve information on common APT groups  
 !hacktool \<search string> - Retrieve information on common hacking tools  
 !cve \<#> - Return the last n CVE's  
 !secnews - (Use as Private Message Only) Latest # of security news articles (default: 10)  
 !vulnnews - (Use as Private Message Only)  Latest # of vulnerability news articles (default: 10)  

 **== Misc ==**

 !stats \<YYYY or YYYY-MM or YYYY-MM-DD> - Produce usage statistics for a day or month (ex: 2017-12)  
 !cc \<Credit Card Number> - Tests validity of a CC number and attempts to determine the brand (ex: 4012888888881881 or 378282246310005)   
 !time \<timezone> - Query time in specified timezone (ex: utc)  
 !weather \<zipcode> - Query the weather in a specified zip code (ex: 21144)  
 !unixtime \<epoch> - Convert Unix time (seconds since Jan 1, 1970) to human readable (ex: 1347517370)  
 !wintime \<epoch> - Convert Windows time (100-nanosecond intervals since January 1, 1601) to human readable (ex: 131580340430000000)  
 !calc \<arithmetic input> - Performs basic arithmetic (Valid input: [0-9]+-/)  (ex: 22*3)  
 !bitcoin - Polls the latest Bitcoin Price Index  
 !whatsyourip - Returns CyBot's public IP Address  
 !joke - Queries an on-line API repository of jokes  
 !codename - Generates a 2 word project codename  


# Setup steps
1)  Download and install errbot:  http://errbot.io/en/latest/user_guide/setup.html#prerequisites

2)  Configure errbot to work with your chat platform:  http://errbot.io/en/latest/user_guide/setup.html#id1  
a)  For help with Slack Setup:  https://github.com/cylance/CyBot/blob/master/CyBot-Arsenal-BH-USA-2019.pdf  
b)  For help with Teams Setup:  http://securitysynapse.blogspot.com/2019/09/cybot-on-microsoft-teams.html  

3)  Download our plugins from this github repo and copy them into the errbot plugins directory

4)  Add VirusTotal and Google Safebrowsing API keys to python scripts

5)  Start errbot


# Additional Props
Errbot developers for the fantastic tool and customer service  
vt - VirusTotal  
hashid  - c0re  
safebrowsing - Google & Jun C. Valdez  
whois - hackertarget[.]com  
geoip - ip-api[.]com  
uastring - useragentstring.com  
ransom - http[:]//goo[.]gl/b9R8DE  
threat / aptgroup / hacktool - huntoperator  
cve - CIRCL https[:]//www[.]circl[.]lu  
secnews/vulnnews - Google News  
cc - David Pany  
time - worldclockapi.com  
weather - wunderground.com  
bitcoin - CoinDesk  
whatsyourip - ipinfo[.]io/ip  
joke - icanhazdadjoke  
codename - Mark Biek  

Black Hat Arsenal team for the amazing support and tool release venue

Others:  Bill Hau, Corey White, Dennis Hanzlik, Ian Ahl, Dave Pany, Dan Dumond, Kyle Champlin, Kierian Evans, Andrew Callow, Mark Stevens
