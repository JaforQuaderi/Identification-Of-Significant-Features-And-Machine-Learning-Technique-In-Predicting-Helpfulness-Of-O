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

number_linguistic_features = 6

linguistic_features_data_array = [[0 for array_column in range(number_linguistic_features)] for array_row in range(number_row_review_dataset)]

k = 0

for rvw in review:
    review_text = rvw.find("review_text").text
    helpful = rvw.find("helpful").text

    # MEASURE HELPFUL VOTES RATIO
    helpful_strip = helpful.strip()
    if not helpful_strip:
        helpful_ratio = 0.0
    else:
        helpful_temp = re.findall(r'\d+', helpful_strip)
        res = list(map(int, helpful_temp))
        helpful_ratio = res[0] / res[1]

    helpful_value = 0
    if helpful_ratio > 0.60:
        helpful_value = 1
    else:
        helpful_value = 0

    # SENTENCE LENGTH
    review_sentence = sent_tokenize(review_text)

    state_verb_list1 = ['like', 'dislike', 'love', 'hate', 'hear', 'imagine',
                        'impress', 'smell', 'see', 'seem', 'sound', 'stay',
                        'suppose', 'taste', 'think', 'understand', 'wish', 'feel',
                        'lack', 'look', 'mind', 'know', 'need', 'believe',
                        'owe', 'deny', 'prefer', 'have', 'doubt', 'resemble',
                        'remember', 'appear', 'satisfy', 'possess', ' please', 'want',
                        'concern', 'weigh', 'grow', 'fit', 'exist', 'include',
                        'involve', 'belong', 'consist', 'contain', 'depend', 'own',
                        'agree', 'disagree', 'mean', 'deserve', 'release', 'measure',
                        'recognise', 'remain', 'turn', 'matter']
    state_verb_list2 = ['am', 'is', 'are', 'was', 'were', 'be', 'been', 'being']

    review_adjective_count = 0
    review_state_verb_count = 0
    review_state_action_verb_count = 0
    review_imperative_action_verb_count = 0
    review_descriptive_action_verb_count = 0

    for sentence_text in review_sentence:

        # POS TAGGING- VERB, ADJECTIVE
        is_verb = lambda pos: pos[:2] == 'VB'
        is_adjective = lambda pos: pos[:2] == 'JJ'

        sentence_text_lower = sentence_text.lower()

        tokenized_marged_string = nltk.word_tokenize(sentence_text_lower)
        verbs_sentence = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_verb(pos)]
        adjectives_sentence = [word for (word, pos) in nltk.pos_tag(tokenized_marged_string) if is_adjective(pos)]

        adjetive_count = 0
        state_action_verb_count = 0
        imperative_action_verb_count = 0
        descriptive_action_verb_count = 0
        state_verb_count = 0

        if len(adjectives_sentence) >= 1:
            adjetive_count = 1

        review_adjective_count = review_adjective_count + adjetive_count

        array_vrbs = [] * len(verbs_sentence)
        array_vrbs_scores = [] * len(verbs_sentence)
        array_vrbs_types = [] * len(verbs_sentence)

        if len(verbs_sentence) == 0:
            state_action_verb_count = 0
            imperative_action_verb_count = 0
            descriptive_action_verb_count = 0
            state_verb_count = 0
        else:
            list_of_words_sentence_in_split = sentence_text_lower.split()
            for vrbs in verbs_sentence:
                if vrbs in state_verb_list1:
                    state_verb_count = 1
                elif vrbs in state_verb_list2:
                    if vrbs in list_of_words_sentence_in_split:
                        try:
                            check_next_word_for_action_verb = \
                                list_of_words_sentence_in_split[list_of_words_sentence_in_split.index(vrbs) + 1]
                            if check_next_word_for_action_verb in state_verb_list1:
                                state_verb_count = 1
                                break
                            elif check_next_word_for_action_verb in state_verb_list2:
                                state_verb_count = 1
                                break
                            else:
                                next_verb_tokenize = nltk.word_tokenize(check_next_word_for_action_verb)
                                next_verb_pos_tagging = nltk.pos_tag(next_verb_tokenize)
                                if next_verb_pos_tagging[0][1] == 'VB' or next_verb_pos_tagging[0][1] == 'VBD' or \
                                        next_verb_pos_tagging[0][1] == 'VBG' or next_verb_pos_tagging[0][1] == 'VBN' or \
                                        next_verb_pos_tagging[0][1] == 'VBP' or next_verb_pos_tagging[0][1] == 'VBZ':
                                    state_verb_count = 0
                                else:
                                    state_verb_count = 1
                        except IndexError:
                            check_next_word_for_action_verb = None
                            state_verb_count = 1
                elif vrbs not in state_verb_list1 and vrbs not in state_verb_list2:
                    try:
                        verb_synset1 = wordnet.synsets(vrbs)[1]
                    except IndexError:
                        verb_synset1 = None

                    try:
                        verb_synset2 = wordnet.synsets(vrbs)[2]
                    except IndexError:
                        verb_synset2 = None

                    try:
                        verb_synset3 = wordnet.synsets(vrbs)[3]
                    except IndexError:
                        verb_synset3 = None

                    verb_synset_score = 0

                    if verb_synset3 is None and verb_synset2 is not None:
                        verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
                        verb_synset2_Text_Blob = TextBlob(verb_synset2.definition())
                        verb_synset_score = (1 / 2) * (
                                verb_synset1_Text_Blob.sentiment.subjectivity + verb_synset2_Text_Blob.sentiment.subjectivity)
                    elif verb_synset2 is None and verb_synset1 is not None:
                        verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
                        verb_synset_score = verb_synset1_Text_Blob.sentiment.subjectivity
                    elif verb_synset1 is None:
                        verb_synset_score = 0
                    else:
                        verb_synset1_Text_Blob = TextBlob(verb_synset1.definition())
                        verb_synset2_Text_Blob = TextBlob(verb_synset2.definition())
                        verb_synset3_Text_Blob = TextBlob(verb_synset3.definition())
                        verb_synset_score = (1 / 3) * (
                                verb_synset1_Text_Blob.sentiment.subjectivity + verb_synset2_Text_Blob.sentiment.subjectivity + verb_synset3_Text_Blob.sentiment.subjectivity)

                    Tao1 = 0.6
                    Tao2 = 0.1

                    action_verb_type = None
                    if verb_synset_score >= Tao1:
                        action_verb_type = 'SAV'
                    elif Tao2 <= verb_synset_score < Tao1:
                        action_verb_type = 'IAV'
                    else:
                        action_verb_type = 'DAV'

                    array_vrbs.append(vrbs)
                    array_vrbs_scores.append(verb_synset_score)
                    array_vrbs_types.append(action_verb_type)

            if len(array_vrbs) == 0:
                state_action_verb_count = 0
                imperative_action_verb_count = 0
                descriptive_action_verb_count = 0
            else:
                max_score_verbs_index, max_score_verbs_value = max(enumerate(array_vrbs_scores),
                                                                   key=operator.itemgetter(1))

                if array_vrbs_types[max_score_verbs_index] == 'DAV':
                    state_action_verb_count = 0
                    imperative_action_verb_count = 0
                    descriptive_action_verb_count = 1
                    state_verb_count = 0
                elif array_vrbs_types[max_score_verbs_index] == 'IAV':
                    state_action_verb_count = 0
                    imperative_action_verb_count = 1
                    descriptive_action_verb_count = 0
                    state_verb_count = 0
                elif array_vrbs_types[max_score_verbs_index] == 'SAV':
                    state_action_verb_count = 1
                    imperative_action_verb_count = 0
                    descriptive_action_verb_count = 0
                    state_verb_count = 0

        review_state_verb_count = review_state_verb_count + state_verb_count
        review_state_action_verb_count = review_state_action_verb_count + state_action_verb_count
        review_imperative_action_verb_count = review_imperative_action_verb_count + imperative_action_verb_count
        review_descriptive_action_verb_count = review_descriptive_action_verb_count + descriptive_action_verb_count

    for l in range(number_linguistic_features):
        if l == 0:
            linguistic_features_data_array[k][l] = review_adjective_count
        elif l == 1:
            linguistic_features_data_array[k][l] = review_state_verb_count
        elif l == 2:
            linguistic_features_data_array[k][l] = review_state_action_verb_count
        elif l == 3:
            linguistic_features_data_array[k][l] = review_imperative_action_verb_count
        elif l == 4:
            linguistic_features_data_array[k][l] = review_descriptive_action_verb_count
        elif l == 5:
            linguistic_features_data_array[k][l] = helpful_value
    k = k + 1

adjective_array = [] * number_row_review_dataset
state_verb_array = [] * number_row_review_dataset
state_action_verb_array = [] * number_row_review_dataset
imperative_action_verb_array = [] * number_row_review_dataset
descriptive_action_verb_array =  [] * number_row_review_dataset
helpful_value_array = [] * number_row_review_dataset

for i in range(0, number_row_review_dataset):
    for j in range(0, number_linguistic_features):
        if j == 0:
            adjective_array.append(linguistic_features_data_array[i][j])
        elif j == 1:
            state_verb_array.append(linguistic_features_data_array[i][j])
        elif j == 2:
            state_action_verb_array.append(linguistic_features_data_array[i][j])
        elif j == 3:
            imperative_action_verb_array.append(linguistic_features_data_array[i][j])
        elif j == 4:
            descriptive_action_verb_array.append(linguistic_features_data_array[i][j])
        elif j == 5:
            helpful_value_array.append(linguistic_features_data_array[i][j])

adjective_mean = statistics.mean(adjective_array)
state_verb_mean = statistics.mean(state_verb_array)
state_action_verb_mean = statistics.mean(state_action_verb_array)
imperative_action_verb_mean = statistics.mean(imperative_action_verb_array)
descriptive_action_verb_mean = statistics.mean(descriptive_action_verb_array)

adjective_stdv = statistics.stdev(adjective_array)
state_verb_stdv = statistics.stdev(state_verb_array)
state_action_verb_stdv = statistics.stdev(state_action_verb_array)
imperative_action_verb_stdv = statistics.stdev(imperative_action_verb_array)
descriptive_action_verb_stdv = statistics.stdev(descriptive_action_verb_array)

adjective_z_score = [] * number_row_review_dataset
state_verb_z_score = [] * number_row_review_dataset
state_action_verb_z_score = [] * number_row_review_dataset
imperative_action_verb_z_score = [] * number_row_review_dataset
descriptive_action_verb_z_score = [] * number_row_review_dataset

for z in range(0, number_row_review_dataset):
    adjective_z_score.append((adjective_array[z] - adjective_mean)/adjective_stdv)
    state_verb_z_score.append(state_verb_array[z] - state_verb_mean/state_verb_stdv)
    state_action_verb_z_score.append(state_action_verb_array[z] - state_action_verb_mean/state_action_verb_stdv)
    imperative_action_verb_z_score.append(imperative_action_verb_array[z] - imperative_action_verb_mean/imperative_action_verb_stdv)
    descriptive_action_verb_z_score.append(descriptive_action_verb_array[z] - descriptive_action_verb_mean/descriptive_action_verb_stdv)

linguistic_features_data_array_generating = [[0 for array_column in range(number_linguistic_features)] for array_row in range(number_row_review_dataset)]

for x in range(0, number_row_review_dataset):
    linguistic_features_data_array_generating[x][0] = adjective_z_score[x]
    linguistic_features_data_array_generating[x][1] = state_verb_z_score[x]
    linguistic_features_data_array_generating[x][2] = state_action_verb_z_score[x]
    linguistic_features_data_array_generating[x][3] = imperative_action_verb_z_score[x]
    linguistic_features_data_array_generating[x][4] = descriptive_action_verb_z_score[x]
    linguistic_features_data_array_generating[x][5] = helpful_value_array[x]

# for x in range(0, number_row_review_dataset):
#     print(linguistic_features_data_array_generating[x])

with open('ln_new_dataset_cleaned_update_27_2_2021.csv', 'w', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    thewriter.writerow(['ADJ', 'SV', 'SAV', 'IAV', 'DAV', 'Helpful'])

with open('ln_new_dataset_cleaned_update_27_2_2021.csv', 'a', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    for d in linguistic_features_data_array_generating: thewriter.writerow(d)