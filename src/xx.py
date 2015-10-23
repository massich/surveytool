def test_bibtexparser():
    import bibtexparser

    with open('../scratch/thesis_methods.bib') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)

    list_of_journals = set([i.get(u'journal') for i in bib_database.entries])
    titles = [i.get(u'title') for i in bib_database.entries]

    for l in list_of_journals:
        print l
    print 'xxxxxxxxxxxxxxxxx'
    for t in titles:
        print t

def test_scholar(xx):
    # Create the querier and its options
    querier = ScholarQuerier()
    settings = ScholarSettings()
    settings.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
    # querier.apply_settings should be in an assert == ture. when false no internet
    querier.apply_settings(settings)

    # Create the query options
    query = SearchScholarQuery()
    query.set_num_page_results(100)
    query.set_words("breast+ultrasound|sonography")
    query.set_words_some("ultrasound sonography, segmentation contouring")
    query.set_timeframe(start=2009)
    query.set_pub(xx)

    print query.get_url()

    # querier.send_query(query)
    # citation_export(querier)


if __name__ == '__main__':
    from scholar.scholar import *
    # from journals import get_target_journals
    # list_of_journals = get_target_journals()
    import pickle
    file = open('journals.txt', 'r')
    list_of_journals = pickle.load(file)
    file.close()
    # print list_of_journals

    test_scholar(list_of_journals[0][u'name'])
    # test_bibtexparser()
