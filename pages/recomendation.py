import os
# define the name of the directory to be created
path = "../Modelo Final"
   
ruta_modelo = path + "/LDA-Model"

from pycaret.nlp import *

lda_final = load_model(ruta_modelo)
num_topics = len(lda_final.get_topics());

import pandas as pd
import pickle


train_data_dir = path + "/train_data_.sav"
train_tokenized_words_dir = path + "/train_tokenized_words.sav"
train_corpus_dir = path + "/train_corpus.sav"
train_id2word_dir = path + "/train_id2word.sav"


test_data_dir = path + "/test/test_data_.sav"
test_tokenized_words_dir = path + "/test/test_tokenized_words.sav"
test_corpus_dir = path + "/test/test_corpus.sav"
test_id2word_dir = path + "/test/test_id2word.sav"


lda_train_results_dir = path + "/lda_train_results.df"
#lda_test_results_dir = path + "/lda_test_results.df"


train_data_ = pickle.load(open(train_data_dir, 'rb'))
train_tokenized_words = pickle.load(open(train_tokenized_words_dir, 'rb'))                                
train_corpus = pickle.load(open(train_corpus_dir, 'rb'))
train_id2word = pickle.load(open(train_id2word_dir, 'rb')) #Diccionario gensin

test_data_ = pickle.load(open(test_data_dir, 'rb'))
test_tokenized_words = pickle.load(open(test_tokenized_words_dir, 'rb'))                                
test_corpus = pickle.load(open(test_corpus_dir, 'rb'))
test_id2word = pickle.load(open(test_id2word_dir, 'rb')) #Diccionario gensin

lda_train_results = pickle.load(open(lda_train_results_dir, 'rb'))
#lda_test_results = pickle.load(open(lda_test_results_dir, 'rb'))



document_topic_matrix_dir = path + "/document_topic_matrix.sav"
topic_word_matrix_dir = path + "/topic_word_matrix.sav"

document_topic_matrix = pickle.load(open(document_topic_matrix_dir, 'rb'))
topic_word_matrix = pickle.load(open(topic_word_matrix_dir, 'rb'))


import extended_similarities as sims
import numpy as np

k = 5

X = np.array(document_topic_matrix)  # pandas to np.array

cos_knn = sims.DistributedCosineKnn(k=k)

indices, distances = cos_knn.fit(input_data=X, n_bucket=10)


#indices
doc = 635

print(indices[doc])
#print(distances[doc])

print(doc)
print()
print(lda_train_results.iloc[doc])
print()
document_topic_matrix.iloc[doc]
print(train_data_.document_title.iloc[doc])
print()
print(train_data_.text.iloc[doc][:1000])