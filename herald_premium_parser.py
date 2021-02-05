#!/bin/env python3
"""
Extracts the article from a "premium" NZ Herald article bypassing the paywall

Written by Nathan McCulloch
"""


from html.parser import HTMLParser
import urllib.request
import sys

NZ_HERALD_URL = ""

class HeraldHTMLParser(HTMLParser):
    current_start_tag = ""
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.current_start_tag = tag
    
    def handle_endtag(self, tag):
        if tag == 'p':
            self.current_start_tag = ''
    
    def handle_data(self, data):
        if self.current_start_tag == 'p':
            print(data)

def printUsageInfo():
    print()
    print("========== NZ Herald Premium Paywall Bypasser ==========")
    print("Tool for bypassing NZ Herald's \"premium\" paywall")
    print("Usage: ./herald_premium_parser.py nz_herald_url")


if len(sys.argv) != 2:
    print("Error: Need a URL as second argument")
    printUsageInfo()
    sys.exit(0)

#Retrieve NZ Herald url from command line arguments
try:
    NZ_HERALD_URL = sys.argv[1]
except:
    printUsageInfo()

req = urllib.request.Request(url=NZ_HERALD_URL)
r = urllib.request.urlopen(req).read()

parser = HeraldHTMLParser()
parser.feed(r)
