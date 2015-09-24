Survey Tool
===========

This tool intends to scraping google scholar, scopus, etc. in order to aid the research process for building up a survey of a topic. We are not the first ones to attempt [this idea][idea]. And one of the problems might be that some [policies might be violated][problems]. I’m not doing apology of evil miss-usage of the search engines. However, research and reading time is scarce enough to be waisted not making use of our best skills and tools.

This project attempts to reduce the amount of papers to be read for any given topic by scraping the website, collecting meta information of the papers and allowing for a better choice on which papers spent your time on.
Take a look at this tools:
* [Scholar.py][scholarpy] allows for querying google scholar. I use it to directly import the BibTex of a reference directly from my editor.
* [gscholar][pdfMatch] takes a pdf file and finds its entry from google shcolar.
* This [tools][tools] might come handy to build up graphs of the references based on some criteria. ([see the comment of its author][more_comments])

Similar tools
-------------
I think this [project][medialab] was doing what I had in mind, but I didn’t manage to make it work, yet. I’ve some issues with mongo and starting the server.

Similar stuff for Scopus
------------------------
https://github.com/argaen/citations_crawler
https://github.com/McKenzieKohn/scopus_spider
https://github.com/giamo/scopus-search-api-client
http://dev.elsevier.com/blog.html



[scholarpy]:https://github.com/ckreibich/scholar.py
[medialab]:https://github.com/medialab/scholarScape#fork-some-code
[pdfMatch]:https://github.com/venthur/gscholar
[tools]:https://github.com/ketch/scinet


[idea]:http://simplystatistics.org/tag/web-scraping/
[problems]:http://academia.stackexchange.com/questions/2567/api-eula-and-scraping-for-google-scholar
[more_comments]:http://academia.stackexchange.com/questions/2520/automatically-building-a-database-of-forward-and-backward-citations/2523#2523
