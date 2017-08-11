#!/usr/bin/env python
#
# Copyright (c) 2016 Jun C. Valdez
# Code is distrubuted under the terms of an MIT style license 
# http://www.opensource.org/licenses/mit-license 
#

import requests
import json 

SB_CLIENT_ID = "Python SafeBrowsing Client"
SB_CLIENT_VER = "0.0.1"


class LookupAPI(object):

    
    def __init__(self, apikey):

        self.apiurl = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=%s' % (apikey)
        self.platform_types = ['ANY_PLATFORM']
        self.threat_types = ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE', 
                             'SOCIAL_ENGINEERING', 
                             'UNWANTED_SOFTWARE', 
                             'POTENTIALLY_HARMFUL_APPLICATION']
        self.threat_entry_types = ['URL']

    def set_threat_types(self, threats):

        self.threat_types = threats

    def set_platform_types(self, platforms): 
        
        self.platform_types = platforms

    def threat_matches_find(self, *urls): 
     
        threat_entries = []
        results = {}
 
        for url_ in urls: 
            url = {'url': url_} 
            threat_entries.append(url)
 
        reqbody = {
            'client': {
                 'clientId': SB_CLIENT_ID,
                 'clientVersion': SB_CLIENT_VER
            },
            'threatInfo': {
                'threatTypes': self.threat_types,
                'platformTypes': self.platform_types,
                'threatEntryTypes': self.threat_entry_types,
                'threatEntries': threat_entries
            }
        }
        
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.apiurl, 
                          data=json.dumps(reqbody), 
                          headers=headers)
        #
        # need to include exceptions here 
        #

        return r.json()



class UpdateAPI(object):


    def __init__(self, apikey):
        pass



