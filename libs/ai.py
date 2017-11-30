import numpy as np
import tensorflow as tf
import tflearn
import spacy
nlp = spacy.load('en')
import re
from nltk.util import ngrams, trigrams
import csv

def build_model():
    # This resets all parameters and variables, leave this here
    tf.reset_default_graph()
    
    #### Your code ####
    net = tflearn.input_data([None, 1200])                          # Input
    net = tflearn.fully_connected(net, 200, activation='ReLU')      # Hidden
    net = tflearn.fully_connected(net, 25, activation='ReLU')      # Hidden
    net = tflearn.fully_connected(net, 2, activation='softmax')   # Output
    net = tflearn.regression(net, optimizer='sgd', learning_rate=0.1, loss='categorical_crossentropy')
    model = tflearn.DNN(net)

    return model

model = build_model()
model.load('./data/model.tfl')

import csv
word2idx = {}
for key, val in csv.reader(open("./data/vocabindex.csv")):
    word2idx[key] = int(val)

def textStringToPOSArray(text):
    doc = nlp(text)
    tags = []
    for word in doc:
        tags.append(word.pos_)
    return tags

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

def getPOSTrigramsForTextString(text):
    tags = textStringToPOSArray(text)
    tgrams = list(trigrams(tags))
    return tgrams

def trigramsToDictKeys(trigrams):
    keys = []
    for trigram in trigrams:
        keys.append('>'.join(trigram))
    return keys

def textToTrigrams(text): 
    return trigramsToDictKeys(getPOSTrigramsForTextString(text))

def text_to_vector(text):
    wordVector = np.zeros(1200)
    for word in textToTrigrams(text):
        index = word2idx.get(word, None)
        if index != None:
            wordVector[index] += 1
    return wordVector

def test_sentence(sentence):
    positive_prob = model.predict([text_to_vector(sentence)])[0][1]
    print('Sentence: {}'.format(sentence))
    print('P(positive) = {:.3f} :'.format(positive_prob), 
          'Positive' if positive_prob > 0.5 else 'Negative')
    return positive_prob