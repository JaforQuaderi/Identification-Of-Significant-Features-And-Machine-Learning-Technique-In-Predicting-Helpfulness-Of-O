"'' ('Bismillahir Rahmanir Rahim') """
import os
from xml.etree import ElementTree
from textblob import TextBlob
import re
import csv
import pandas as pd
pd.set_option('display.max_rows', 500000)

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

number_subjectivity_features = 2

subjectivity_features_data_array_generating = [[0 for array_column in range(number_subjectivity_features)] for array_row in range(number_row_review_dataset)]

k = 0

for rvw in review:
    review_txt = rvw.find("review_text").text
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

    # SUBJECTIVITY
    Review_Text_Blob = TextBlob(review_txt)
    subjectivity_score = Review_Text_Blob.sentiment.subjectivity

    for l in range(number_subjectivity_features):
        if l == 0:
            subjectivity_features_data_array_generating[k][l] = subjectivity_score
        elif l == 1:
            subjectivity_features_data_array_generating[k][l] = helpful_value
    k = k + 1

for s in subjectivity_features_data_array_generating:
    print(s)

with open('sb_new_dataset_cleaned_update_27_2_2021.csv', 'w', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    thewriter.writerow(['SUBJECTIVITY', 'Helpful'])

with open('sb_new_dataset_cleaned_update_27_2_2021.csv', 'a', newline='') as file_CSV:
    thewriter = csv.writer(file_CSV)
    for d in subjectivity_features_data_array_generating: thewriter.writerow(d)