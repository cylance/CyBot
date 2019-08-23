# !cuckoo interacts with a Cuckoo API

import re, os, subprocess, datetime, requests, json, pyminizip
from requests.exceptions import HTTPError
from collections import Counter
from errbot import BotPlugin, botcmd, arg_botcmd

server="changeme"
port="8090"
headers = {"Authorization": "AuthTokenHere"}
#VT Private API Key
vtapikey="changeme"



## FUNCTION:  CUCKOO STATUS ##
def cuckoo_status(results):
    results = results + "\r\nFunction:  Status Query\r\n"
    REST_URL=server + ":" + port + "/cuckoo/status"
    #print(REST_URL)
    r = requests.get(REST_URL, headers=headers)
    if r.status_code == 200:
        #print(r)
        data = r.json()
        #print(data)
        results = results + json.dumps(data, sort_keys=True, indent=4)
    else:
        results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)
    return(results)


## FUNCTION  CUCKOO TASK VIEW ##
def cuckoo_view(results, args):
    results = results + "\r\nFunction:  View Status\r\n"
    if not len(args)==2:
        return("Incorrect number of parameters.  View Function requires a task ID (number) as a parameter.")
        exit()
    elif args[1].isdigit():
        REST_URL=server + ":" + port + "/tasks/view/" + args[1]
        r = requests.get(REST_URL, headers=headers)
        if r.status_code == 200:
            data = r.json()
            results = results + re.sub('\.', '\[\.\]', json.dumps(data, sort_keys=True, indent=4))
        else:
            results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)
    else:
        return("Incorrect parameter type.  View Function requires a task ID (number) as a parameter.")
    return(results)


## FUNCTION  CUCKOO REPORT VIEW ##
def cuckoo_report(results, args):
    results = results + "\r\nFunction:  Report Fetch\r\n"
    if not len(args)==2:
        return("Incorrect number of parameters.  Report Function requires a task ID (number) as a parameter.")
        exit()
    elif args[1].isdigit():
        REST_URL=server + ":" + port + "/tasks/report/" + args[1]
        r = requests.get(REST_URL, headers=headers)
        if r.status_code != 200:
            results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)
        else:
            results+="Full report most likely located here: " + server + ":8080/analysis/" + args[1] + "\r\n"
            obj = r.json()
            results+="## ==== INFO ====" + "\r\n"
            results+="ID: " + str(obj["info"]["id"]) + "\r\n"
            results+="Score: " + str(obj["info"]["score"]) + " of 10.\r\n"
            results+="Duration: " + str(obj["info"]["duration"]) + " seconds \r\n"
            results+="Machine Name: " + str(obj["info"]["machine"]["name"]) + "\r\n"

            results+="\r\n## ==== TARGET ====" + "\r\n"
            if str(obj['target']['category'])=="url":
                for c in obj['target']:
                    if c=="url":
                        results+=c + ": "+ re.sub('\.', '\[\.\]', str(obj['target'][c])) + "\r\n"
                    else:
                        results+=c + ": " + str(obj['target'][c]) + "\r\n"
            elif str(obj['target']['category'])=="file":
                results+="category: file\r\n"
                for c in obj['target']['file']:
                    results+=c + ": " + str(obj['target']['file'][c]) + "\r\n"
            else:
                return("Category is not file or url.  It is:  " + str(obj['target']['category']))

            results+="\r\n## ==== Cuckoo Signatures ====" + "\r\n"
            for c in obj['signatures']:
                results+=c['description'] + "  (Severity: " + str(c['severity']) + ")\r\n"

            vterror=0

            results+="\r\n## ==== VirusTotal ====" + "\r\n"
            for c in obj['virustotal']['summary']:
                results+=c + ": " + str(obj['virustotal']['summary'][c]) + "\r\n"
                if c=="error":
                    vterror=1

            if vterror==0:
                for c in obj['virustotal']['scans']:
                    if str(obj['virustotal']['scans'][c]['detected'])!="False":
                        results+=c + ": " + str(obj['virustotal']['scans'][c]['result']) + "\r\n"

            results+="\r\n## ==== Dropped Files ====" + "\r\n"
            if 'dropped' not in obj:
                results+="No dropped files"
            else:
                for c in obj['dropped']:
                    #results+=c['sha256'] + " - " + c['name'] + "\r\n"
                    yay="fota"
    else:
        return("Incorrect parameter type.  View Function requires a task ID (number) as a parameter.")
    return(results)


## FUNCTION  CUCKOO PROCESS URL ##
def cuckoo_url(results, args):
    results = results + "\r\nFunction: URL Query"
    if not len(args)==2:
        return("Incorrect number of parameters.  URL Function requires a single URL as a parameter.  Defanged URLS accepted [] or ().")
        exit()
    else:
        url=args[1]
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
            return("Be sure to submit a valid URL.  This plugin requires only one argument of a full URL to include protocol. Defanged URLS accepted [] or ().")

        data = {"url": url}
        REST_URL=server + ":" + port + "/tasks/create/url"
        r = requests.post(REST_URL, headers=headers, data=data)
        if r.status_code == 200:
            task_id = r.json()["task_id"]
            results = results + "\r\nSuccess!\r\ntask_id = " + str(task_id)
        else:
            results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)
        return(results)


## FUNCTION  CUCKOO PROCESS FILE ##
## ATTEMPTED TO MAKE THIS FUNCTION SUBMIT PASSWORD PROTECTED ZIP FILES, BUT CUCKOO WILL NOT PERFORM VT LOOKUP ##
def cuckoo_file(results, args):
    results = results + "\r\nFunction:  VirusTotal File Query"
    if not len(args)==2:
        return("Incorrect number of parameters.  VirusTotal File Function requires a single hash as a parameter.")
        exit()
    file_hash=args[1]
    if not (re.findall(r"(^[a-fA-F\d]{32}$)", file_hash) or re.findall(r"(^[a-fA-F\d]{40}$)", file_hash) or re.findall(r"(^[a-fA-F\d]{64}$)", file_hash)):
    # print("false")
        if not (len(file_hash)==32 or len(file_hash)==40 or len(file_hash)==64):
            return("MD5 hashes are 32, SHA1 hashes are 40, and SHA256 hashes are 64 characters in length.  Your submission is " + str(len(file_hash)) + " characters.  Please try again.")
        else:
            return("You have the right number of characters (32, 40, or 64) (Your hash length is: " + str(len(file_hash)) + "), but one of your characters is not a valid hash character of:  a-f, A-F, 0-9.")
    
    url = "https://www.virustotal.com/vtapi/v2/file/download?apikey=" + vtapikey + "&hash=" + file_hash
    fullPath = "/tmp/" + file_hash
    #zipPath = fullPath + ".zip"
    #outputName = file_hash + ".zip"
    answer = "Fetching file: " + file_hash

    try:
    # Fetch the file
        response = requests.get(url)
        response.raise_for_status()
        # Check to see if VT has the file
        if response.status_code == 200:
            results = results + "\r\nReceived HTTP 200.  VirusTotal has the file!\r\n"
            with open(fullPath, 'wb') as f:
                f.write(response.content)

            # zip with password of infected, rename as hash.zi_
            #results = results + "Zipping the file with a password of: infected\r\n"
            #pyminizip.compress(fullPath, "", zipPath, "infected", 1)

            REST_URL=server + ":" + port + "/tasks/create/file"
            #print(REST_URL)

            #with open(zipPath, "rb") as sample:
            with open(fullPath, "rb") as sample:
                files = {"file": ("temp_file_name", sample)}
                r = requests.post(REST_URL, headers=headers, files=files)
            
            if r.status_code == 200:
                #print(r)
                data = r.json()
                #print(data)
                results = results + json.dumps(data, sort_keys=True, indent=4)
            else:
                results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)

            deleteFile = "rm -f " + fullPath
            os.system(deleteFile)
            #deleteFile = "rm -f " + outputName
            #os.system(deleteFile)
        else:
            results = results + "\r\nERROR:  Received HTTP response code of: " + str(r.status_code)

    except requests.exceptions.HTTPError as error:
        if re.search(r'Not Found', str(error)):
            return("Error:  It appears that VirusTotal does not have this file.")
        else:
            return("Something went wrong.  Do you have Internet?  Do you have pyminizip installed?  Did you enter an API Key?")
        exit()
    return(results)

## END OF HELPER FUNCTIONS ##


class cuckoo(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def cuckoo(self, msg, args):
        if not len(args)>=1:
            return("Incorrect number of parameters.  Syntax:  !cuckoo -<s | u <Defanged_URL> | vt <hash> | v <task_id> | r <task_id>>\r\n!cuckoo -s (provides Cuckoo status)\r\n!cuckoo -u <Defanged_URL> (runs a URL - [.] and (.) accepted)\r\n!cuckoo -vt <hash> (downloads a file from VT and runs the file\r\n!cuckoo -v <task_id> (views stats of task)\r\n!cuckoo -r <task_id> (views report for task)")
            exit()

        if server=="changeme":
            return("Error:  Cuckoo server not configured in script.  This plugin will not work until fixed.")

        # Assign arguments to variables 
        function=args[0]

        # Check function
        fvalid = re.match(r'^-s$', function) or re.match(r'^-u$', function) or re.match(r'^-vt$', function) or re.match(r'^-v$', function) or re.match(r'^-r$', function)
        if not fvalid:
            return("Incorrect function.  Syntax:  !cuckoo -<s | u <Defanged_URL> | vt <hash> | v <task_id> | r task_id>>\r\n!cuckoo -s (provides Cuckoo status)\r\n!cuckoo -u <Defanged_URL> (runs a URL - [.] and (.) accepted)\r\n!cuckoo -vt <hash> (downloads a file from VT and runs the file\r\n!cuckoo -v <task_id> (views a task)\r\n!cuckoo -r <task_id> (views report for task)")
            exit()

        results="Querying Cuckoo Server: " + server + ":" + port

        ##################  STATUS QUERY  ################## 
        if re.match(r'^-s$', function):
            results=cuckoo_status(results)

        ##################  URL QUERY  ################## 
        elif re.match(r'^-u$', function):
            results=cuckoo_url(results, args)

        ##################  FILE QUERY  ################## 
        elif re.match(r'^-vt$', function):
            if vtapikey=="changeme":
                return("Error:  Private VirusTotal API Key not configured in script.  This function will not work until fixed.")
            else:
                results=cuckoo_file(results, args)

        ##################  VIEW QUERY  ################## 
        elif re.match(r'^-v$', function):
            results=cuckoo_view(results, args)
        
        ##################  REPORT QUERY  ################## 
        elif re.match(r'^-r$', function):
            results=cuckoo_report(results, args)
        
        else:
            return("No Function Match.")
            exit()

        return(results)

