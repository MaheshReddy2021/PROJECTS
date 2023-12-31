# -*- coding: utf-8 -*-
"""Fake News Prediction With Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2IynfBRgpOpMkpDP8Z11-OENA9E_S5B
"""

import numpy as np
import pandas as pd
import re     #Regular expression library --> useful for searching words in a tex or paragraph
from nltk.corpus import stopwords #Natural language tool kit   stopwards--->words which does not give a value to pargraph or text
from nltk.stem.porter import PorterStemmer   #gives us rootword for a particular word
from sklearn.feature_extraction.text import TfidfVectorizer  # text into feature vexctors
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns

"""About The dataset

     id: unique id for a news article
     title: the title of a news article
     author: author of the news article
     text: the text of the article; could be incomplete
     label: a label that marks the article as potentially unreliable
    1 : Fake news
    0 : Real news

Data Pre-processing
"""

dataset = pd.read_csv("//content/train.csv.zip")

dataset.head()

dataset.shape

# total number of missing values in the dataset
dataset.isnull().sum()

#null values are replaced by empty string
dataset = dataset.fillna("")

dataset["new_data"] = dataset["author"]+" "+dataset["title"]

print(dataset.new_data)

X = dataset.drop(columns="label", axis=1)

Y = dataset["label"]

print(X)
print(Y)

"""Stemming:

Stemming is the process of reducing a word to its Root word

eg:
    actor,actress,acting ----> act
"""

import nltk
nltk.download("stopwords")

#printing the stopwords in English
print(stopwords.words("english"))

port_stem_news = PorterStemmer()

def stemming(new_data):
  stemmed_new_data = re.sub('[^a-zA-Z]'," ", new_data) # ^ exclusion--->only everything wil be removed except alphabetes and " " is used to replce numbers and other things
  stemmed_new_data = stemmed_new_data.lower()
  stemmed_new_data = stemmed_new_data.split()
  stemmed_new_data = [port_stem_news.stem(word) for word in stemmed_new_data if not word in stopwords.words("english")]
  stemmed_new_data = " ".join(stemmed_new_data)
  return stemmed_new_data

dataset["new_data"] = dataset["new_data"].apply(stemming)

print(dataset["new_data"])

# Seperating the data and label

X = dataset["new_data"].values

Y = dataset["label"].values

print(X)

print(Y)

Y.shape

# converting the textual data to numerical data

vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

print(X)

"""Splitting the dataset training and test data"""

X_train, X_test,Y_train,Y_test = train_test_split(X, Y, test_size = 0.2 , stratify = Y, random_state = 2) # stratify--> split the data in the same proportion as original dataset

"""Training the Model : Logistic Regreession"""

news_model = LogisticRegression()

news_model.fit(X_train,Y_train)

"""Evaluation

accuracy score
"""

X_train_prediction = news_model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print("Accuracy score of the training data : " , training_data_accuracy)

X_test_prediction = news_model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print("Accuracy score of the test data : ", test_data_accuracy)

"""Confusion matrix"""

cf_matrix = confusion_matrix(Y_test, X_test_prediction)

print(cf_matrix)

tn, fp ,fn ,tp = cf_matrix.ravel()

print(tn, fp, fn, tp)

"""Heat map"""

sns.heatmap(cf_matrix, annot = True)

# Here 73 predicted values shows false positive and 14 predicted values shows false negative
# 2004 predicted values shows true negative and 2069 shows true positve

"""Predictive system"""

X_new = X_test[4]

prediction = model.predict(X_new)

print(prediction)


if(prediction[0]==0):

  print("News is Real")
else:

  print("News is Fake")

print(X_test[4])