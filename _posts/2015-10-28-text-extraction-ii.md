---
layout: post
title: "text extraction II"
description: ""
category: 
tags: []
---
{% include JB/setup %}

The [slate](https://github.com/timClicks/slate) package did not work for me.
First, we had some issues with the [PDFMiner](https://github.com/euske/pdfminer)
version and once we made it work, the outputted text was really dirty with
plenty of estrange characters and no spaces at all between words.

The [PyPDF2](http://mstamy2.github.io/PyPDF2/) package is not intended to
extract text from the PDF but manipulating the document itself by performing
operations like cropping, copying, rotating etc..

So we decided to directly use **PDFMiner** and make the helper functions we
need to wrap around it.
