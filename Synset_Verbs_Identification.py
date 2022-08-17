"'' print ('Bismillahir Rahmanir Rahim') """
import math
import os
from xml.etree import ElementTree

import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.regexp import WhitespaceTokenizer

import textstat
import re

from textblob import TextBlob
import spacy

from textatistic import Textatistic

import csv

from nltk.corpus import sentiwordnet as swn

nlp = spacy.load('en_core_web_lg')

from nltk.corpus import wordnet

string_text = 'anger'

# verb_synset1 = wordnet.synsets(string_text)[1]
# verb_synset2 = wordnet.synsets(string_text)[2]
# verb_synset3 = wordnet.synsets(string_text)[3]

try:
    verb_synset1 = wordnet.synsets(string_text)[1]
    print('Passed 1')
except IndexError:
    verb_synset1 = None
    print('Passed 1 Fail')

try:
    verb_synset2 = wordnet.synsets(string_text)[2]
    print('Passed 2')
except IndexError:
    verb_synset2 = None
    print('Passed 2 Fail')

try:
    verb_synset3 = wordnet.synsets(string_text)[3]
    print('Passed 3')
except IndexError:
    verb_synset3 = None
    print('Passed 3 Fail')

verb_synset_score = 0;

print(type(verb_synset3))

if verb_synset3 is None and verb_synset2 is not None:
    verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
    verb_synset2_Text_Blob = TextBlob(verb_synset2.definition())
    verb_synset_score = (1 / 2) * (verb_synset1_Text_Blob.sentiment.subjectivity + verb_synset2_Text_Blob.sentiment.subjectivity)
    print(verb_synset_score)
elif verb_synset2 is None and verb_synset1 is not None:
    verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
    verb_synset_score = verb_synset1_Text_Blob.sentiment.subjectivity
    print(verb_synset_score)
elif verb_synset1 is None:
    verb_synset_score = 0
    print(verb_synset_score)
else:
    verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
    verb_synset2_Text_Blob = TextBlob(verb_synset2.definition())
    verb_synset3_Text_Blob = TextBlob(verb_synset3.definition())
    verb_synset_score = (1 / 3) * (verb_synset1_Text_Blob.sentiment.subjectivity + verb_synset2_Text_Blob.sentiment.subjectivity + verb_synset3_Text_Blob.sentiment.subjectivity)
    print(verb_synset_score)

Tao1 = 0.6
Tao2 = 0.1

action_verb_type = None
if verb_synset_score >= Tao1:
    action_verb_type = 'SAV'
elif Tao2 <= verb_synset_score < Tao1:
    action_verb_type = 'IAV'
else:
    action_verb_type = 'DAV'

print(action_verb_type)