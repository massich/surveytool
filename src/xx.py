import bibtexparser

with open('../scratch/thesis_methods.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)
print(bib_database.entries)
