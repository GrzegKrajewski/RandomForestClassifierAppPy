import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import PyQt5 as pq
from sklearn.ensemble import RandomForestClassifier

dict_column_names={'Age': "age", "AnnualIncome": "annual_income", "FamilyMembers":"family_members", "ChronicDiseases" :"is_chronic_diseases",
                   "Employment Type_Private Sector/Self Employed": "is_self_employed", "GraduateOrNot_Yes": "is_graduated",
                   "FrequentFlyer_Yes":"is_frequent_flyer", "EverTravelledAbroad_Yes": "is_ever_travelled_abroad"}

import os
from pathlib import Path

file_name="X.csv"
X=pd.read_csv(file_name)
file_name="y.csv"
y=pd.read_csv(file_name)
y=y.values.ravel()

X=X.rename(columns=dict_column_names)

class_rf=RandomForestClassifier(class_weight='balanced')
class_rf.fit(X,y)

import pickle
from datetime import datetime
current_path = os.path.abspath(os.path.dirname(__file__))

path_to_save='model_RF.pickle'
model={'model':class_rf,'name':'RandomForest'+datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
with open(os.path.join(current_path,path_to_save), 'wb') as model_file:
    pickle.dump(model, model_file)