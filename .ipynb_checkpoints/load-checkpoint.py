#This file is the backbone of the chatbot and uses deeplearning to get a probability for a matching tag based on a user's input
#Does all the processing of the data and feeds it to a neural network.
import nltk     #nltk to process sentences
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn      #tflearn to more easily work with tensorflow
import tensorflow   #to create a neural network that will create an output that is a probability of a tag matching an input sentence
import random       
import json         #for importing the json file with all our intents
import pickle       #to store our data as a pickle file, so we don't have to process it everytime

#loads in the files and data we need, returns data, models, words, and labels
class load:
    def __init__(self,f):
        #load in the json file
        with open(f) as file:
            data = json.load(file)
        self.data = data
    

    def Process(self):
        #try to open the data.pickle file, if it can't it will process the json file
        try:
            with open("data.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            words =  []
            labels = []
            docs_x = []
            docs_y = []
            data = self.data

            #we grab all the patterns from the intents file and process them by tokenizing all the words, removing ?, . , !, stemming the words
            #and sorting them into a list, removing the duplicates.
            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])
            ignore_words = ['?', '.', '!']
            words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
            words = sorted(list(set(words)))

            labels = sorted(labels)

            training = []
            output = []

            out_empty = [0 for _ in range(len(labels))]

            for x, doc in enumerate(docs_x):
                bag = []

                wrds = [stemmer.stem(w.lower()) for w in doc]

                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(output_row)

            #if the file opens successfully, we can skip all word processing
            training = numpy.array(training)
            output = numpy.array(output)

            with open("data.pickle", "wb") as f:
                pickle.dump((words, labels, training, output), f)
        #tensorflow with 4 fully connected networks, each with 8 nodes. The data is run 1000 times through the net and comes out with a
        #98%+ accuracy rate
        tensorflow.compat.v1.reset_default_graph()

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)
        #try to load the tflearn model if it exists, as not to have to run all the data again, else run it and save the model
        try:
            model.load("model.tflearn")
        except:
            model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
            model.save("model.tflearn")
        self.words = words
        self.model = model
        self.labels = labels


    #the bag of words creates a 1 hot encoded array, where whenever a word matches, the array will increment that position of a similar sized
    #array from "0" to "1"
    #returns a numpy array as this is what tensorflow works with
    def bag_of_words(self,s,words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
            
        return numpy.array(bag)


    #getters for data,model,words,labels for use in chatbot.py
    def getData(self):
        return self.data

    def getModel(self):
        return self.model

    def getWords(self):
        return self.words
    
    def getLabels(self):
        return self.labels

   