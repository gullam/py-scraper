#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Sources import Sources
from ScraperUtils import ScraperUtils

'''
Main Class
Leads.py, by Gullam Hussain, 20 Apr, 2016
'''


# Main method
def main():
    keyphrase = raw_input("Search Phrase: ")
    keyphrase = ScraperUtils.normalize_input(keyphrase)
    source = Sources(keyphrase)
    leads = source.get_leads()
    seen = set()
    for lead in leads:
        if lead.url not in seen:
            relevancyScore = abs(100-lead.relevance)*0.01
            print "➢", lead.url, " (", relevancyScore, ")"
            seen.add(lead.url)


if __name__ == '__main__':
    main()
