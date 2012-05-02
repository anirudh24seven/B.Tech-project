Sentiment Classification using WSD
==================================

Overview
--------

Sentiment Classifier using Word Sense Disambiguation using ``wordnet`` and word occurance
statistics from movie review corpus ``nltk``. Classifies into positive and negative categories.

Requirements
------------

- You must have Python 2.6 with argparse http://pypi.python.org/pypi/argparse
- NLTK http://www.nltk.org  2.0 installed. 
- NumPy http://numpy.scipy.org
- SentiWordNet http://sentiwordnet.isti.cnr.it

How to Install
--------------
Shell command::

  python setup.py install

Documentation
-------------
http://packages.python.org/sentiment_classifier/::
  
  sentiment_classifier/src/senti_classifier/documentation.html
  

How to Use
==========
Script Usage
------------
Shell Commands::

  senti_classifier -p path_to/SentiWordNet_3.0.0_20100908.txt 
  Success, Pickled Sentiwordnet to -->  SentiWn.p
  senti_classifier -c reviews.txt

Python Usage
------------
Shell Commands::

  cd sentiment_classifier/src/senti_classifier/
  python senti_classifier.py -p path_to/SentiWordNet_3.0.0_20100908.txt
  python senti_classifier.py -c reviews.txt


History
=======

-` `0.4`` Added Bag of Words as a Feature as occurance statistics
- ``0.3`` Sentiment Classifier First app, Using WSD module

To-Do
-----

Classify using option ``neutral`` as custom heuristic.
