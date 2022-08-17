"'' ('Bismillahir Rahmanir Rahim') """
from textatistic import Textatistic
import textstat
import os
import re
from xml.etree import ElementTree
import readability
import csv

file_name = 'dataset_cleaned.xml'
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

number_readability_features = 11

readability_features_data_array_generating = [[0 for array_column in range(number_readability_features)] for array_row in range(number_row_review_dataset)]

k = 0

for rvw in review:
    review_text = rvw.find("review_text").text
    helpful = rvw.find("helpful").text
    asin = rvw.find("asin").text

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

    readability_score = Textatistic(review_text).scores
    r = readability.getmeasures(review_text, lang='en')

    Flesch_Kincaid_Grade_Level_Score = readability_score['fleschkincaid_score']
    Smog_Index_Score = readability_score['smog_score']
    Gunning_Fog_Index_Score = readability_score['gunningfog_score']
    Automated_Readability_Score = textstat.automated_readability_index(review_text)
    Colemen_Liau_Index_Score = textstat.coleman_liau_index(review_text)

    Flesch_Kincaid_Score = r['readability grades']['Kincaid']
    Flesch_Reading_Ease_Score = r['readability grades']['FleschReadingEase']
    Dale_Chall_Index_Score = r['readability grades']['DaleChallIndex']
    LIX_Score = r['readability grades']['LIX']
    RIX_Score = r['readability grades']['RIX']


    for l in range(number_readability_features):
        if l == 0:
            readability_features_data_array_generating[k][l] = Flesch_Kincaid_Grade_Level_Score
        elif l == 1:
            readability_features_data_array_generating[k][l] = Smog_Index_Score
        elif l == 2:
            readability_features_data_array_generating[k][l] = Gunning_Fog_Index_Score
        elif l == 3:
            readability_features_data_array_generating[k][l] = Automated_Readability_Score
        elif l == 4:
            readability_features_data_array_generating[k][l] = Colemen_Liau_Index_Score
        
        elif l == 5:
            readability_features_data_array_generating[k][l] = Flesch_Kincaid_Score
        elif l == 6:
            readability_features_data_array_generating[k][l] = Flesch_Reading_Ease_Score
        elif l == 7:
            readability_features_data_array_generating[k][l] = Dale_Chall_Index_Score
        elif l == 8:
            readability_features_data_array_generating[k][l] = LIX_Score
        elif l == 9:
            readability_features_data_array_generating[k][l] = RIX_Score

        elif l == 10:
            readability_features_data_array_generating[k][l] = helpful_value
            
    k = k + 1

with open('rd_all_dataset_cleaned_update_12_2_2021.csv', 'w', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    thewriter.writerow(['FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'FK', 'FER', 'DCI', 'LIX', 'RIX', 'Helpful'])

with open('rd_all_dataset_cleaned_update_12_2_2021.csv', 'a', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    for d in readability_features_data_array_generating: thewriter.writerow(d)