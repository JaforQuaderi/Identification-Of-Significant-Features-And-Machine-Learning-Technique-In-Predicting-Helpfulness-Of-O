import numpy as np
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn import datasets
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.svm import SVC


pd.set_option('display.max_rows', 30000)

cross_val_value = 10
test_data_size = 0.2


# ### Linguistic, Readability and Subjectivity Features
# csv_file = pd.read_csv("ad_ln_rd_sb_bdekh_npu_update_27_1_2021.csv")
# x = csv_file[['ADJ', 'SV', 'SAV', 'IAV', 'DAV', 'FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'SUBJECTIVITY']]
# y = csv_file['Helpful']
#
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_data_size, random_state=42)
# svm_model = svm.SVC(kernel='linear', C=1, random_state=42).fit(X_train, y_train)
# svm_model_scores = cross_val_score(svm_model, x, y, cv=cross_val_value)
# print("SVM: ", svm_model_scores.mean()*100)
#
# rf_model = RandomForestClassifier(max_depth=None, random_state=42)
# rf_model_scores = cross_val_score(rf_model, x, y, cv=cross_val_value)
# print("RF:  ", rf_model_scores.mean()*100)
#
# nb_model = GaussianNB()
# nb_model_scores = cross_val_score(nb_model, x, y, cv=cross_val_value)
# print("NB:  ", nb_model_scores.mean()*100)
#
# dt_model = DecisionTreeClassifier(max_depth=None, random_state=42)
# dt_model_scores = cross_val_score(dt_model, x, y, cv=cross_val_value)
# print("DT:  ", dt_model_scores.mean()*100)

### Linguistic, Readability and Subjectivity Features
csv_file = pd.read_csv("dataset_krs_linguistic_readability_metadata_subjectivity_polarity_features.csv")
# x = csv_file[['ADJ', 'SV', 'SAV', 'IAV', 'DAV', 'FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'Subjectivity', 'Polarity', 'Length', 'NOUN', 'ADVERB', 'Rating', 'Capitalized_Words', 'Number_Sentences', 'Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation']]
# x = csv_file[['Adjective', 'Noun', 'Adverb', 'SV', 'SAV', 'IAV', 'DAV', 'FK', 'DCI', 'LIX', 'RIX', 'Subjectivity', 'Polarity', 'Length', 'Rating', 'Capitalized_Words', 'Number_Sentences', 'Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation']]
## Linguistic Features
# x = csv_file[['Noun', 'Adverb', 'Adjective', 'SV', 'SAV', 'IAV', 'DAV', 'Length', 'Capitalized_Words', 'Number_Sentences']]

## Readability Features
# x = csv_file[['FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'FK', 'FER', 'DCI', 'LIX', 'RIX']]

## Metadata Subjectivity Polarity Features
# x = csv_file[['Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation', 'Subjectivity', 'Polarity', 'Rating']]
## linguistic_linguistic_readability_readability_metadata_subjectivity_polarity_features
x = csv_file[['Noun', 'Adverb', 'Adjective', 'SV', 'SAV', 'IAV', 'DAV', 'Length', 'Capitalized_Words', 'Number_Sentences', 'FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'FK', 'FER', 'DCI', 'LIX', 'RIX', 'Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation', 'Subjectivity', 'Polarity', 'Rating', 'FKGL', 'SMOGI', 'GFI', 'ARI', 'CLI', 'FK', 'FER', 'DCI', 'LIX', 'RIX', 'Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation', 'Rating']]
y = csv_file['Helpful']



X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_data_size, random_state=42)
svm_model = svm.SVC(kernel='linear', C=1, random_state=42).fit(X_train, y_train)
svm_model_scores = cross_val_score(svm_model, x, y, cv=cross_val_value)
print("SVM: ", svm_model_scores.mean()*100)

rf_model = RandomForestClassifier(max_depth=None, random_state=42)
rf_model_scores = cross_val_score(rf_model, x, y, cv=cross_val_value)
print("RF:  ", rf_model_scores.mean()*100)

nb_model = GaussianNB()
nb_model_scores = cross_val_score(nb_model, x, y, cv=cross_val_value)
print("NB:  ", nb_model_scores.mean()*100)

dt_model = DecisionTreeClassifier(max_depth=None, random_state=42)
dt_model_scores = cross_val_score(dt_model, x, y, cv=cross_val_value)
print("DT:  ", dt_model_scores.mean()*100)

import winsound
duration = 2000  # milliseconds
freq = 500  # Hz
for tone in range (0, 10):
    winsound.Beep(freq, duration)