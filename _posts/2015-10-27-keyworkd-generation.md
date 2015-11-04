---
layout: post
title: "keyword generation"
description: ""
category: 
tags: []
---
{% include JB/setup %}

From each article we want to extract all the keywords that refer to the methodology proposal and evaluation. In this manner, we can study afterwards all the collected keywords and prepare our methodology comparison.

### What are we looking for?
We are looking for automatically extracting information in terms of keywords such as: Active contours, Level-Set, Texture, Optimization, ICM, Graph-cut, LBP, thershold, 8-Neighbours, Area Overlap, Otshu ...

So we need to go from a full text, to a dictionary of keywords that actually describe the methodology.

#### What to use?
Based on some googling it seems that [NLTK](http://www.nltk.org/) is the way to go ([here is stackOverflow post](http://stackoverflow.com/questions/22543523/research-papers-classification-on-the-basis-of-title-of-the-research-paper) supporting this affirmation).
To my understand, NLTK is a low-level library that extract language elements at sentence level and needs to be combined with other packages such as **sckit-learn** to make an statistic study. **NLTK** offers great flexibility and the task we want to perform is detailed in [this book](http://www.nltk.org/book_1ed/) (the 2nd edition is planed by 2016), however we might need something more straight forward and let a deeper language study for later on.

At this point, we have moved to explore libraries that are able to automatically tag text or use snippets using **NLTK**. If this is not enough, we’ll come back to **NLTK**.
So far here are some tools to explore:

  - [ Article ](http://conjugateprior.org/software/ca-in-python/) showing how to get keywords in context for content analysis
  - Using **NLTK**

    - [NLTK example](http://stackoverflow.com/questions/2661778/tag-generation-from-a-text-content)
    - [Demonstration of extracting key phrases with NLTK in Python](https://gist.github.com/alexbowe/879414)
    - [tokenizer](http://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/), see the accompanying [snippet](https://gist.github.com/shlomibabluki/5539628)
    - [extract keywords](https://www.quora.com/How-can-I-extract-keywords-from-a-document-using-NLTK)
    - [rake algorithm with **NLTK**](http://sujitpal.blogspot.fr/2013/03/implementing-rake-algorithm-with-nltk.html)
    - [chapter 5 of NLTK book](http://www.nltk.org/book/ch05.html)

  - [tagger](https://github.com/apresta/tagger)
  - [Automatic-tag-generator](https://github.com/pratyush-nigam/Automatic-Tag-Generator)

## Also take a look at:

[corpkit](http://interrogator.github.io/corpkit/) can also be used. It has a [GUI](http://interrogator.github.io/corpkit/) to dynamicaly explore text corpora.
