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


    def _get_info(issn):
        import urllib2
        # Import BeautifulSoup -- try 4 first, fall back to older
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            try:
                from BeautifulSoup import BeautifulSoup
            except ImportError:
                print('We need BeautifulSoup, sorry...')
                sys.exit(1)

        # def _get_header(initial_soup):
        #     parts = initial_soup.find_all("div", class_="col-md-12")
        #     return BeautifulSoup(parts[1])

        # def _extract_full_name(header):
        url = 'http://www.issn.cc/{0:s}'.format(issn)
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), "html.parser")
        tag = soup.find_all("div", class_="col-md-12")
        header = tag[1].findChildren()
        body = tag[3].find("dl").findChildren()
        # header = BeautifulSoup(tag[1], "html.parser")
        # body = BeautifulSoup(tag[3], "html.parser").find("div", class_="body")

        return {u'issn':issn,
                u'issn_url':url,
                u'name':header[-1].string,
                u'abbr':body[1].string,
                u'other_abbr':body[7],
                u'lang':body[-3].string,
                u'url':body[-1]}

    target_journals_issn = ['0031-9155', '0161-7346', '0278-0062', '0895-6111', '1361-8415', '1861-6410']
    return [ _get_info(x) for x in target_journals_issn ]



if __name__ == "__main__":
    for x in get_target_journals():
        print '|[{0:s}]|[{1:s}]|{2:s}|'.format(x[u'issn'], x[u'name'], x[u'abbr'])

    for x in get_target_journals():
        print '[{0:s}]: {1:s}'.format(x[u'issn'],x[u'issn_url'])
        print '[{0:s}]: {1:s}'.format(x[u'name'],x[u'url'])
