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
import itertools
from collections import defaultdict
from gensim import corpora

inputFolder = 'D:\\Phelps\\GitHub\\AnyQ\\tools\\simnet\\preprocess\\data\\'
outputFolder = inputFolder

train = pd.read_csv(inputFolder + "train.csv")  # 共404290个问句对
#test = pd.read_csv("data/test.csv")

# Check for any null values
#print(train.isnull().sum())

# Add the string 'empty' to empty strings
train = train.fillna('empty')
#test = test.fillna('empty')

stop_words = ['the','a','an','and','but','if','or','because','as','what','which','this','that','these','those','then',
              'just','so','than','such','both','through','about','for','is','of','while','during','to','What','Which',
              'Is','If','While','This']

def text_to_wordlist(text, remove_stop_words=True, stem_words=False):
    # Clean the text, with the option to remove stop_words and to stem words.

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"what's", "", text)
    text = re.sub(r"What's", "", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r" m ", " am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"60k", " 60000 ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e-mail", "email", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"quikly", "quickly", text)
    text = re.sub(r" usa ", " America ", text)
    text = re.sub(r" USA ", " America ", text)
    text = re.sub(r" u s ", " America ", text)
    text = re.sub(r" uk ", " England ", text)
    text = re.sub(r" UK ", " England ", text)
    text = re.sub(r"india", "India", text)
    text = re.sub(r"switzerland", "Switzerland", text)
    text = re.sub(r"china", "China", text)
    text = re.sub(r"chinese", "Chinese", text) 
    text = re.sub(r"imrovement", "improvement", text)
    text = re.sub(r"intially", "initially", text)
    text = re.sub(r"quora", "Quora", text)
    text = re.sub(r" dms ", "direct messages ", text)  
    text = re.sub(r"demonitization", "demonetization", text) 
    text = re.sub(r"actived", "active", text)
    text = re.sub(r"kms", " kilometers ", text)
    text = re.sub(r"KMs", " kilometers ", text)
    text = re.sub(r" cs ", " computer science ", text) 
    text = re.sub(r" upvotes ", " up votes ", text)
    text = re.sub(r" iPhone ", " phone ", text)
    text = re.sub(r"\0rs ", " rs ", text) 
    text = re.sub(r"calender", "calendar", text)
    text = re.sub(r"ios", "operating system", text)
    text = re.sub(r"gps", "GPS", text)
    text = re.sub(r"gst", "GST", text)
    text = re.sub(r"programing", "programming", text)
    text = re.sub(r"bestfriend", "best friend", text)
    text = re.sub(r"dna", "DNA", text)
    text = re.sub(r"III", "3", text) 
    text = re.sub(r"the US", "America", text)
    text = re.sub(r"Astrology", "astrology", text)
    text = re.sub(r"Method", "method", text)
    text = re.sub(r"Find", "find", text) 
    text = re.sub(r"banglore", "Banglore", text)
    text = re.sub(r" J K ", " JK ", text)
    
    
    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])
    
    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionally, shorten words to their stems
    if stem_words:
        text = text.split()
        stemmer = SnowballStemmer('english')
        stemmed_words = [stemmer.stem(word) for word in text]
        text = " ".join(stemmed_words)
    
    # Return a list of words
    return(text)

def process_questions(question_list, questions, question_list_name, dataframe):
    '''transform questions and display progress'''
    for question in questions:
        question_list.append(text_to_wordlist(question))
        if len(question_list) % 100000 == 0:
            progress = len(question_list)/len(dataframe) * 100
            print("{} is {}% complete.".format(question_list_name, round(progress, 1)))
            
train_question1 = []
process_questions(train_question1, train.question1, 'train_question1', train)

train_question2 = []
process_questions(train_question2, train.question2, 'train_question2', train)

#test_question1 = []
#process_questions(test_question1, test.question1, 'test_question1', test)
#
#test_question2 = []
#process_questions(test_question2, test.question2, 'test_question2', test)


# Preview some transformed pairs of questions
a = 0 
#for i in range(a,a+10):
#    print(train_question1[i])
#    print(train_question2[i])
#    print()
	
	
raw_corpus = list(itertools.chain.from_iterable([train_question1,train_question2]))
#[train_question1,train_question2]

stoplist = stop_words
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]


frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
        
precessed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

# dictionary
dictionary = corpora.Dictionary(precessed_corpus)
#print(dictionary)
#print(dictionary.token2id)

new_doc = "would happen Indian government stole Kohinoor Koh i Noor diamond back"
new_vec = dictionary.doc2bow(new_doc.lower().split())
#dictionary.doc2idx(new_doc.lower().split())
#print(new_vec)  


bow_corpus = [dictionary.doc2idx(text) for text in precessed_corpus]

bow_corpus_plus_1 = [[i+1 for i in bow_corpu] for bow_corpu in bow_corpus]
bow_corpus_str = [[str(i) for i in bow_corpu_plus] for bow_corpu_plus in bow_corpus_plus_1]
bow_corpus_join = [' '.join(bow_corpus_) for bow_corpus_ in bow_corpus_str]

# 生成文件
pointwise_train = pd.DataFrame(bow_corpus_join[:404290], columns = ['question1'])
pointwise_train['question2'] = bow_corpus_join[404290:]
pointwise_train['is_duplicate'] = train['is_duplicate']

# 防止空(null)问题
pointwise_train = pointwise_train[[len(i)>0 for i in pointwise_train['question1']]]
pointwise_train = pointwise_train[[len(i)>0 for i in pointwise_train['question2']]]

# 拆分训练集和测试集
size = round(len(pointwise_train)*0.8) # 比例为8:2

# tsv格式的数据文件
pointwise_train[:size].to_csv(outputFolder + 'train_.tsv',sep = '\t', index=False, header=False)
pointwise_train[size:].to_csv(outputFolder + 'test_.tsv',sep = '\t', index=False, header=False)

print('finished')  
