"'' ('Bismillahir Rahmanir Rahim') """
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

from nltk.corpus import wordnet

import operator

import statistics

nlp = spacy.load('en_core_web_lg')

file_name = 'new_dataset_cleaned.xml'
full_file = os.path.abspath(os.path.join('Data', file_name))

dom = (ElementTree.parse(full_file))

review = dom.findall('review')

number_row_review_dataset = 0
for rvw in review:
    review_counter = rvw.find("review_text").text
    if not review_counter:
        number_row_review_dataset = 0
    else:
        number_row_review_dataset = number_row_review_dataset+1

# adjective_array = [] * number_row_review_dataset
# adjective_z_score = [] * number_row_review_dataset

# noun_array = [] * number_row_review_dataset
# noun_z_score = [] * number_row_review_dataset

adverb_array = [] * number_row_review_dataset
adverb_z_score = [] * number_row_review_dataset

# verb_array = [] * number_row_review_dataset
# verb_z_score = [] * number_row_review_dataset

# verb_array_review = [] * number_row_review_dataset

k = 0

for rvw in review:
    review_text = rvw.find("review_text").text

    # SENTENCE LENGTH
    review_sentence = sent_tokenize(review_text)

    # review_adjective_count = 0
    # review_noun_count = 0
    review_adverb_count = 0
    # review_verb_count = 0

    for sentence_text in review_sentence:

        # POS TAGGING- NOUN, ADJECTIVE, ADVERB

        total_verbs_sentence = 0

        # is_adjective_jj = lambda pos: pos[:2] == 'JJ'
        # is_adjective_jjr = lambda pos: pos[:2] == 'JJR'
        # is_adjective_jjs = lambda pos: pos[:2] == 'JJS'

        # is_noun_nn = lambda pos: pos[:2] == 'NN'
        # is_noun_nns = lambda pos: pos[:2] == 'NNS'
        # is_noun_nnp = lambda pos: pos[:2] == 'NNP'
        # is_noun_nnps = lambda pos: pos[:2] == 'NNPS'

        is_adverb_rb = lambda pos: pos[:2] == 'RB'
        is_adverb_rbr = lambda pos: pos[:2] == 'RBR'
        is_adverb_rbs = lambda pos: pos[:2] == 'RBS'

        # is_verb_vb = lambda pos: pos[:2] == 'VB'
        # is_verb_vbd = lambda pos: pos[:2] == 'VBD'
        # is_verb_vbg = lambda pos: pos[:2] == 'VBG'
        # is_verb_vbn = lambda pos: pos[:2] == 'VBN'
        # is_verb_vbp = lambda pos: pos[:2] == 'VBP'
        # is_verb_vbz = lambda pos: pos[:2] == 'VBZ'

        sentence_text_lower = sentence_text.lower()

        tokenized_marged_string = nltk.word_tokenize(sentence_text_lower)
        # adjectives_sentence_jj = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adjective_jj(pos)]
        # adjectives_sentence_jjr = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adjective_jjr(pos)]
        # adjectives_sentence_jjs = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adjective_jjs(pos)]

        # nouns_sentence_nn = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_noun_nn(pos)]
        # nouns_sentence_nns = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_noun_nns(pos)]
        # nouns_sentence_nnp = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_noun_nnp(pos)]
        # nouns_sentence_nnps = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_noun_nnps(pos)]

        adverbs_sentence_rb = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adverb_rb(pos)]
        adverbs_sentence_rbr = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adverb_rbr(pos)]
        adverbs_sentence_rbs = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adverb_rbs(pos)]

        # verbs_sentence_vb = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if (pos == 'vb')]
        # verbs_sentence_vbd = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb_vbd(pos)]
        # verbs_sentence_vbg = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb_vbg(pos)]
        # verbs_sentence_vbn = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb_vbn(pos)]
        # verbs_sentence_vbp = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb_vbp(pos)]
        # verbs_sentence_vbz = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb_vbz(pos)]

        # total_verbs_sentence = len(verbs)
                               # + len(verbs_sentence_vbd) + len(verbs_sentence_vbg) + len(verbs_sentence_vbn) + len(verbs_sentence_vbp) + len(verbs_sentence_vbz)

        # adjective_count = 0
        #
        # if len(adjectives_sentence_jj) >= 1 or len(adjectives_sentence_jjr) >= 1 or len(adjectives_sentence_jjs) >= 1:
        #     adjective_count = 1
        #
        # review_adjective_count = review_adjective_count + adjective_count

        # noun_count = 0
        #
        # if len(nouns_sentence_nn) >= 1 or len(nouns_sentence_nns) >= 1 or len(nouns_sentence_nnp) >= 1 or len(nouns_sentence_nnps) >= 1:
        #     noun_count = 1
        #
        # review_noun_count = review_noun_count + noun_count

        adverb_count = 0

        if len(adverbs_sentence_rb) >= 1 or len(adverbs_sentence_rbr) >= 1 or len(adverbs_sentence_rbs) >= 1:
            adverb_count = 1

        review_adverb_count = review_adverb_count + adverb_count

        # verb_count = 0
        #
        # if len(verbs_sentence_vb) >= 1 or len(verbs_sentence_vbd) >= 1 or len(verbs_sentence_vbg) >= 1 or len(verbs_sentence_vbn) >= 1 or len(verbs_sentence_vbp) >= 1 or len(verbs_sentence_vbz) >= 1:
        #     verb_count = 1

        # review_verb_count = review_verb_count + verb_count

    adverb_array.append(review_adverb_count)
    # adjective_array.append(review_adjective_count)
    # noun_array.append(review_noun_count)
    # verb_array_review.append(total_verbs_sentence)

# adjective_mean = statistics.mean(adjective_array)
# adjective_stdv = statistics.stdev(adjective_array)
# for adj in range(0, number_row_review_dataset):
#     adjective_z_score.append((adjective_array[adj] - adjective_mean)/adjective_stdv)

# noun_mean = statistics.mean(noun_array)
# noun_stdv = statistics.stdev(noun_array)
# for nn in range(0, number_row_review_dataset):
#     noun_z_score.append((noun_array[nn] - noun_mean)/noun_stdv)

adverb_mean = statistics.mean(adverb_array)
adverb_stdv = statistics.stdev(adverb_array)
for adv in range(0, number_row_review_dataset):
    adverb_z_score.append((adverb_array[adv] - adverb_mean)/adverb_stdv)

# verb_mean = statistics.mean(verb_array)
# verb_stdv = statistics.stdev(verb_array)
# for v in range(0, number_row_review_dataset):
#     verb_z_score.append((verb_array[v] - verb_mean)/verb_stdv)


# for adj in adjective_z_score:
#     print(adj)

# for nn in noun_z_score:
#     print(nn)

for adv in adverb_z_score:
    print(adv)

# for v in verb_array_review:
#     print(v)

# print("-------------------")
# print(linguistic_features_data_array)
#
# adjective_array = [] * number_row_review_dataset
# state_verb_array = [] * number_row_review_dataset
# state_action_verb_array = [] * number_row_review_dataset
# imperative_action_verb_array = [] * number_row_review_dataset
# descriptive_action_verb_array =  [] * number_row_review_dataset
#
# for i in range(0, number_row_review_dataset):
#     for j in range(0, number_linguistic_features):
#         if j == 0:
#             adjective_array.append(linguistic_features_data_array[i][j])
#         elif j == 1:
#             state_verb_array.append(linguistic_features_data_array[i][j])
#         elif j == 2:
#             state_action_verb_array.append(linguistic_features_data_array[i][j])
#         elif j == 3:
#             imperative_action_verb_array.append(linguistic_features_data_array[i][j])
#         elif j == 4:
#             descriptive_action_verb_array.append(linguistic_features_data_array[i][j])
#
# adjective_mean = statistics.mean(adjective_array)
#
# print("-------------------")
# print(adjective_mean)
#
# print("-------------------")
#
# adjective_stdv = statistics.stdev(adjective_array)
# print(adjective_stdv)
# adjective_z_score = [] * number_row_review_dataset
# for z in range(0, number_row_review_dataset):
#     adjective_z_score.append((adjective_array[z] - adjective_mean)/adjective_stdv)
#
# print("-------------------")
# print(adjective_z_score)
