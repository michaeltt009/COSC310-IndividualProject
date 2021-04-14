#This file contains the acutall chat function of the bot and focuses on the input and ouput
#If need be, chatbot calls load.py to load in all the data that it needs to run
from load import load  #import load function from load.py
import numpy           #numpy for use of numpy.argmax 
import random          #random for grabbing a random response from the matching tag


#load in the json file
l = load("intents.json")
#save all data and tflearn models to use when calculating probabilites
data = l.getData()
l.Process()
model = l.getModel()
words = l.getWords()
labels = l.getLabels()


#for now this method prints out the response, but once we implment a gui, it should return the response instead
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        #results will hold the predicted value of the tags in corrispondence with the user's input    
        results = model.predict([l.bag_of_words(inp, words)])[0]
        #Grab the highest result and store it in results_index
        results_index = numpy.argmax(results)
        #we then can grab the tag belonging to the highest result
        tag = labels[results_index]
        #You can run the below line to see the probability % of each tag that matches in results, and the tag that has the max probability.
        #print(results)
        #print(tag)

        #Check if the probablitu is higher than a set amount, we use 0.8 here to determine if we want to bot to give a random
        #response or for it to say "it didn't understand"
        if results[results_index] > 0.8:
            for t in data["intents"]:
                if t['tag'] == tag:
                    responses = t['responses']

            print(random.choice(responses))
        else:
            print("I didn't quite understand")


#call chat function
chat()

