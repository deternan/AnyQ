# -*- coding: utf-8 -*-

import os
os.chdir("D:\\Phelps\\GitHub\\AnyQ\\tools\\simnet\\preprocess") 	# quora.py的路径

import pandas as pd
import numpy as np

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
from string import punctuation

train = pd.read_csv("D:\\Phelps\\GitHub\\AnyQ\\tools\\simnet\\preprocess\\data\\train.csv")  # 共404290个问句对
#test = pd.read_csv("data/test.csv")

# Check for any null values
print(train.isnull().sum())

# Add the string 'empty' to empty strings
train = train.fillna('empty')
#test = test.fillna('empty')

# Preview some of the pairs of questions
a = 0 
for i in range(a,a+10):
    print(train.question1[i])
    print(train.question2[i])
    print()