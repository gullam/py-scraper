#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter
import urllib
import collections
from ScraperUtils import ScraperUtils

'''
Class to have the main scraper functionalities
Sources.py, by Gullam Hussain, 20 Apr, 2016
'''


class Sources:
    context = ""
    Leads = []
    Lead = collections.namedtuple("Lead", ["title", "content", "url", "relevance"])

    # Constructor
    def __init__(self, context):
        self.set_context(context)

    # This is the public method to get all the leads for the given key phrase
    def get_leads(self):
        self.set_leads_from_google()
        self.set_leads_from_bing()
        return sorted(self.Leads, key=attrgetter('relevance'))

    '''
    Method to scrap the Google results
    TODO: this needs to be modified to make it generic for all sources, using rules/schemas/configs
    '''

    def set_leads_from_google(self):
        if self.context != "":
            src_url = "https://www.google.com/search?num=50&q=" + urllib.quote_plus(self.context)
            soup = ScraperUtils.get_web_content(src_url)
            container = soup.find("div", {"id": "ires"})
            results = container.findAll("div", {"class": "g"})
            index = 0
            for result in results:
                if result.get("id") is not None:
                    continue
                url = result.find("h3", {"class": "r"}).a.get("href")
                title = result.find("h3", {"class": "r"}).a.string
                description = result.string
                if ScraperUtils.is_valid_lead(url, title):
                    index += 1
                    self.Leads.append(self.Lead(title, repr(description), url, index))

    '''
    Method to scrap the Bing results
    TODO: this needs to be modified to make it generic for all sources, using rules/schemas/configs
    '''

    def set_leads_from_bing(self):

        if self.context != "":
            src_url = "http://www.bing.com/search?q=" + urllib.quote_plus(self.context)
            # print src_url
            soup = ScraperUtils.get_web_content(src_url)
            container = soup.find("ol", {"id": "b_results"})
            results = container.findAll("li", {"class": "b_algo"})
            index = 0
            for result in results:
                if result.next.name != 'h2':
                    continue
                url = result.find("h2").a.get("href")
                title = result.find("h2").a.string
                description = result.string
                if ScraperUtils.is_valid_lead(url, title):
                    index += 1
                    self.Leads.append(self.Lead(title, repr(description), url, index))
        return

    # Setter method for context
    def set_context(self, context):
        self.context = context.strip()

    # Getter method for context
    def get_context(self):
        return self.context
