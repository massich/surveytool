from layout_scanner.layout_scanner import *


def parse_lttext_objs (lt_objs, page_number, text=[]):
    """Iterate through the list of LT* objects and capture only the text"""
    text_content = []

    page_text = {} # k=(x0, x1) of the bbox, v=list of text strings within that bbox width (physical column)
    for lt_obj in lt_objs:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            # text, so arrange is logically based on its column width
            page_text = update_page_text_hash(page_text, lt_obj)
        elif isinstance(lt_obj, LTFigure):
            # LTFigure objects are containers for other LT* objects, so recurse through the children
            text_content.append(parse_lttext_objs(lt_obj, page_number, text_content))

    for k, v in sorted([(key,value) for (key,value) in page_text.items()]):
        # sort the page_text hash by the keys (x0,x1 values of the bbox),
        # which produces a top-down, left-to-right sequence of related columns
        text_content.append(''.join(v))

    return '\n'.join(text_content)


def _parse_pages_textonly (doc):
    """With an open PDFDocument object, get the pages and parse only
    LTTextBox elements found at each page
    [this is a higher-order function to be passed to with_pdf()]"""
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    text_content = []
    for i, page in enumerate(PDFPage.create_pages(doc)):
        interpreter.process_page(page)
        # receive the LTPage object for this page
        layout = device.get_result()
        # layout is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.
        text_content.append(parse_lttext_objs(layout, (i+1)))

    return text_content

def get_text(pdf_doc, pdf_pwd=''):
    """Process each of the pages in this pdf file and return a list of strings
    representing the text found in each page without parsing the images"""
    return with_pdf(pdf_doc, _parse_pages_textonly, pdf_pwd)

def process_text(text_list):
    """Takes get_text output and cleans it"""
    from types import StringType
    from re import sub as _substitute
    from string import printable as _printable

    def _remove_non_printables(s):
        """Takes a string and strips all non printable characters"""
        assert type(s) is StringType, "s is not a string"

        regexp = '[^{0:s}]'.format(_printable)
        return _substitute(regexp, '', s)

    def _remove_hyphens_from_word_brakes(s):
        """Remove hyphens due to line break"""
        assert type(s) is StringType, "s is not a string"
        return _substitute('-\n', '', s)

    def _clean(text_line):
        """Help function to drive the text cleaning"""
        x = _remove_non_printables(text_line)
        x = _remove_hyphens_from_word_brakes(x)
        return x

    return map(_clean, text_list)

def process_doc_structure(text_list):
    """Takes get_text output and cleans it"""

    def _remove_non_printables(s):
        """Takes a string and strips all non printable characters"""
        assert type(s) is StringType, "s is not a string"

        regexp = '[^{0:s}]'.format(_printable)
        return _substitute(regexp, '', s)

    def _remove_hyphens_from_word_brakes(s):
        """remove hyphens due to line break"""
        assert type(s) is StringType, "s is not a string"
        return _substitute('-\n', '', s)

    def _take_out_headers(text_list):
        """This function takes a list of paragraphs returns two list of
        paragraphs text and headers.  Headers are assumed to be repeated
        paragraphs along the document"""
        from collections import Counter
        c = Counter(text_list)
        headers = [item for item, count in c.items() if count > 1]
        text = list(set(c.keys()).difference(set(headers)))

        return (text, headers)

    def _select_large_paragraph(text_list, char_length_th=40):
        """From one text list return two text list containing large and short
        paragraphs with respect to char_length_th

        Usually short text would correspond to page numbers, section titles, etc..
        """
        x = zip(text_list, [len(t) for t in text_list])
        large_text = [t for t, char_length in x if char_length > char_length_th]
        short_text = list(set(text_list).difference(set(large_text)))

        return (large_text, short_text)


    text = reduce(lambda x,y: x+y, text_list)
    (text, headers) = _take_out_headers(text.split('\n\n'))
    (text, short_text) = _select_large_paragraph(text)
    # text = _remove_hyphens(text)

    return (text, short_text, headers)
    # return [paragraph for paragraph in text.split('\n\n')]

if __name__ == '__main__':
    t = get_text("../scratch/papers/cui_2009.pdf")
    tt = process_text(t)
    print tt
