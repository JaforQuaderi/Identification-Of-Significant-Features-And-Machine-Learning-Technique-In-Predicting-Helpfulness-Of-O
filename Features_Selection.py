import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif


pd.set_option('display.max_rows', 12000)

cross_val_value = 10
test_data_size = 0.2

csv_file = pd.read_csv("ln_rd_sb_new_dataset.csv")
# x = csv_file[['Adjective', 'Noun', 'Adverb', 'Verb', 'FK', 'DCI', 'LIX', 'RIX', 'Subjectivity', 'Polarity', 'Length', 'Rating', 'Capitalized_Words', 'Number_Sentences', 'Reviewer_Name_Existence', 'Reviewer_Name_Validation', 'Reviewer_Location_Existence', 'Reviewer_Location_Validation']]
x = csv_file[['Adjective', 'Noun', 'Adverb', 'SV', 'SAV', 'IAV', 'DAV', 'Subjectivity', 'Polarity', 'ARI', 'Length', 'Rating', 'Capitalized_Words', 'Number_Sentences']]
y = csv_file['Helpful']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_data_size, random_state=42)

def select_features(X_train, y_train, X_test):
    fs = SelectKBest(score_func=f_classif, k='all')
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs

X_train_fs, X_test_fs, fs = select_features(X_train, y_train, X_test)
for i in range(len(fs.scores_)):
    print('%f' % (fs.scores_[i]))

Features = ['Adjective', 'Noun', 'Adverb', 'SV', 'SAV', 'IAV', 'DAV', 'Subjectivity', 'Polarity', 'ARI', 'Length', 'Rating', 'Capitalized_Words', 'Number_Sentences']

for f in Features:
    print(f)






