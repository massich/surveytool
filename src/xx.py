def get_target_journals():
    """Find the ISSN of the Journals that appear at Journal Citation Reports (JCR) 2014
    under both categories: Engineering Biomedical and radiology"""
    # Import url request
    try:
        # Try importing for Python 3
        # pylint: disable-msg=F0401
        # pylint: disable-msg=E0611
        from urllib.request import Request
    except ImportError:
        # Fallback for Python 2
        from urllib2 import Request

    # Import BeautifulSoup -- try 4 first, fall back to older
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        try:
            from BeautifulSoup import BeautifulSoup
        except ImportError:
            print('We need BeautifulSoup, sorry...')
            sys.exit(1)

    

    target_journals_issn = ['0031-9155', '0161-7346', '0278-0062', '0895-6111', '1361-8415', '1861-6410']


import bibtexparser

with open('../scratch/thesis_methods.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

list_of_journals = set([i.get(u'journal') for i in bib_database.entries])
print list_of_journals




# import scholarly

# xx=[x for x in scholarly.search_author('massich')]


# # Retrieve the author's data, fill-in, and print
# search_query = scholarly.search_author('Steven A Cholewiak')
# author = next(search_query).fill()
# print author

# # Print the titles of the author's publications
# print [pub.bib['title'] for pub in author.publications]

# # Take a closer look at the first publication

# print pub

# # Which papers cited that publication?
# print [citation.bib['title'] for citation in pub.citedby()]



#### ####
from scholar.scholar import *

querier = ScholarQuerier()
settings = ScholarSettings()

settings.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
querier.apply_settings(settings)

query = SearchScholarQuery()
query.set_pub()



