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
    
    def _get_http(issn):
        req = Request(url='http://www.issn.cc/{0:s}'.format(issn))
        


    target_journals_issn = ['0031-9155', '0161-7346', '0278-0062', '0895-6111', '1361-8415', '1861-6410']

