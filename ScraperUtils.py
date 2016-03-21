#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2

'''
Utilities class to have the common utility methods
ScraperUtils.py, by Gullam Hussain, 20 Apr, 2016
'''


class ScraperUtils:
    # Constructor
    def __init__(self):
        pass

    # Method to get the contents/source of the given url
    @staticmethod
    def get_web_content(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        req = urllib2.Request(url, headers=hdr)

        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page.read())
        return soup

    # Method to clean the results retrieved from the websites
    @staticmethod
    def is_valid_lead(url, title):
        invalid_url_set = ["www.google.", "youtube.com", "wikipedia.org", "dictionary.com", ".org\/",
                           "patent", "encyclopedia", "blog.", "google.co", ".edu", "article", "book", "newswire.com"]
        for txt in invalid_url_set:
            if url.find(txt) >= 0:
                return False
        return True

    # Method to remove duplicates from List
    @staticmethod
    def remove_duplicates(values):
        output = []
        seen = set()
        for value in values:
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output

    # Method to normalize input
    @staticmethod
    def normalize_input(str):
        return str

