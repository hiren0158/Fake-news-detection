# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


#reading the train file
df=pd.read_excel("Static/DatasetsUsed/Train.xlsx")

labels=df.Label
#labels.head()
#df.shape

"""x_ans is the variable used for storing the user output.For right now,have put a decoy value

"""

y_train=df['Label']
x_train=df['News']
x_ans=np.array(["The economic turnaround started at the end of my term."])

#Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.8)
#Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_ans)

#Initialize a LogisticRegressor
model= LogisticRegression()
model.fit(tfidf_train,y_train)

y_pred=model.predict(tfidf_test)
#y_pred[0]

file=open("model.pck",'wb')
pickle.dump(model,file)
file.close()

