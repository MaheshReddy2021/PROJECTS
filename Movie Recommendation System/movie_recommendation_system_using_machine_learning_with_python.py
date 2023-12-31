# -*- coding: utf-8 -*-
"""Movie Recommendation System Using Machine Learning With Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dm9ZYAINrDkOxFtvlZyUu8XTjqh7CHH6
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#Here difflib library helps to find the closest match to the user input
#cosine_similarity hepls to find the similarity score to the user input movie.

# loading the dataset from the csv file to a pandas Dataframe.
movies_dataset = pd.read_csv('/content/movies.csv')

movies_dataset.shape

# printing thr first 5 rows of the Dataframe.
movies_dataset.head()

movies_dataset.isnull().sum()

# Replaceing the null values with null string
movies_dataset_selected_features = ["genres" ,"keywords", "tagline" , "cast" , "director" , "overview"]
print(movies_dataset_selected_features)

for movies_feature in movies_dataset_selected_features:
  movies_dataset[movies_feature] = movies_dataset[movies_feature].fillna('')

# after replace the null values with null string

movies_dataset.isnull().sum()

movies_dataset_combined_features = movies_dataset["genres"]+movies_dataset["keywords"]+movies_dataset["tagline"]+movies_dataset["cast"]+movies_dataset["director"]+movies_dataset["overview"]+movies_dataset["spoken_languages"]

print(movies_dataset_combined_features)

movies_vectorizer = TfidfVectorizer()
# now coverting the text data into numerical values

movies_dataset_feature_vectors = movies_vectorizer.fit_transform(movies_dataset_combined_features)

print(movies_dataset_feature_vectors)

"""Cosine Similarity"""

# getting the similarity scores using cosine similarity

movies_dataset_similarity = cosine_similarity(movies_dataset_feature_vectors)

print(movies_dataset_similarity)

print(movies_dataset_similarity.shape)

# movie name from the user input

movie_name = input("Enter your favourite movie name : ")

# creating a list with all the movie names given in the dataset

movies_dataset_list_of_all_titles = movies_dataset["title"].tolist()

print(movies_dataset_list_of_all_titles)

# finding the close match for the movie name given by the user

find_close_match = difflib.get_close_matches(movie_name, movies_dataset_list_of_all_titles)

print(find_close_match)

close_match = find_close_match[0]

print(close_match)

# finding the index of the movie with title

index_of_the_movie = movies_dataset[movies_dataset.title == close_match]["index"].values[0]

print(index_of_the_movie)

# getting the list of similar movies

similarity_score = list(enumerate(movies_dataset_similarity[index_of_the_movie]))

print(similarity_score)

len(similarity_score)

# sorting the movies based on their similarity score

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print(sorted_similar_movies)

# print the name of similar movies based on the index

print("Movies suggested for you : \n")

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_dataset[movies_dataset.index==index]["title"].values[0]
  if(i<30):
    print(i, "_",title_from_index)
    i+=1

"""Movies Recommendation System"""

movie_name = input("Enter your favourite movie name : ")

movies_dataset_list_of_all_titles = movies_dataset["title"].tolist()

find_close_match = difflib.get_close_matches(movie_name, movies_dataset_list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_dataset[movies_dataset.title == close_match]["index"].values[0]

similarity_score = list(enumerate(movies_dataset_similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print("Movies suggested for you : \n")

i = 1

for movie in sorted_similar_movies:

  index = movie[0]
  title_from_index = movies_dataset[movies_dataset.index==index]["title"].values[0]
  if(i<30):
    print(i, "_",title_from_index)
    i+=1

