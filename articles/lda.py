import os
from pycaret.nlp import *
import pandas as pd
import pickle
import extended_similarities as sims
import numpy as np

# define the name of the directory to be created
path = "../modelo_final"   
ruta_modelo = path + "/LDA-Model"
# definicion directorios de resultados de entrenamiento
lda_final = load_model(ruta_modelo)
num_topics = len(lda_final.get_topics())
num_words = 25
topics = lda_final.show_topics(formatted=True, num_topics=num_topics, num_words=num_words)



train_data_dir = path + "/train_data_.sav"
train_tokenized_words_dir = path + "/train_tokenized_words.sav"
train_corpus_dir = path + "/train_corpus.sav"
train_id2word_dir = path + "/train_id2word.sav"
lda_train_results_dir = path + "/lda_train_results.df"

#Cargar los resultados del modelo
train_data_ = pickle.load(open(train_data_dir, 'rb'))
train_tokenized_words = pickle.load(open(train_tokenized_words_dir, 'rb'))                                
train_corpus = pickle.load(open(train_corpus_dir, 'rb'))
train_id2word = pickle.load(open(train_id2word_dir, 'rb')) #Diccionario gensin


lda_train_results = pickle.load(open(lda_train_results_dir, 'rb'))
topics_train = [lda_final[train_corpus[i]] for i in range(len(train_data_))]

def topics_document_to_dataframe(topics_document, num_topics):
    res = pd.DataFrame(columns=range(num_topics))
    for topic_weight in topics_document:
        res.loc[0, topic_weight[0]] = topic_weight[1]
    return res

def document_topic_matrix():

    document_topic_matrix = \
    pd.concat([topics_document_to_dataframe(topics_document, num_topics=num_topics) for topics_document in topics_train]) \
        .reset_index(drop=True).fillna(0)
    return document_topic_matrix

def topic_word_matrix():
    topic_word_matrix = pd.DataFrame(lda_final.get_topics(), columns=lda_final.id2word.values(), index=[i for i in range(num_topics)])
    return topic_word_matrix

def top_doc_per_topic(topic , top):

    return lda_train_results.sort_values(topic, ascending=False)[topic].head(top)




document_topic_matrix_dir = path + "/document_topic_matrix.sav"
topic_word_matrix_dir = path + "/topic_word_matrix.sav"

document_topic_matrix = pickle.load(open(document_topic_matrix_dir, 'rb'))
topic_word_matrix = pickle.load(open(topic_word_matrix_dir, 'rb'))

print('asd')

k = 10

X = np.array(document_topic_matrix)  # pandas to np.array

cos_knn = sims.DistributedCosineKnn(k=k)

indices, distances = cos_knn.fit(input_data=X, n_bucket=10)

doc = 123

print(indices[doc])

#for index in indices[doc]:
#    print(indices[index])


#print(doc)
#print()
#print(lda_train_results.iloc[doc])
#print()
#document_topic_matrix.iloc[doc]
#print(train_data_.document_title.iloc[doc])
#print()
#print(train_data_.text.iloc[doc][:1000])