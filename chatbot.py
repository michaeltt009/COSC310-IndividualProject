#This file contains the actual chat function of the bot and focuses on returning the appropriate output to gui.py
#If need be, chatbot calls load.py to load in all the data that it needs to run

from load import load #import load function from load.py        
from load import load #import load function from load.py
from sentiment import sentiment #import sentiment function from sentiment.py
from translate import translate #import translate class from translate.py
from twitter import twitter     #import twitter class from twitter.py
import numpy #numpy for use of numpy.argmax 
import random #random for grabbing a random response from the matching tag
from syn_recognition import synonym_sentences # import synonym_sentences function from syn_recognition.py

#load in the json file
l = load("intents.json")
#save all data and tflearn models to use when calculating probabilites
data = l.getData()
l.Process()
model = l.getModel()
words = l.getWords()
labels = l.getLabels()


#This method takes in user input from the Entry box in the GUI, and returns an appropriate response from the bot.
def chat(user_inp, *args):
    while True:
        #Get user input
        inp = user_inp
        if not inp:
            return "Please say something!"

        #instantiates translate object
        trans = translate(inp)
        isInFrench = False

        if(trans.detectFrench() == True):       #if the input is detected to be in french
            isInFrench = True                   #variable to check if original input was in french
            inp = trans.translateFRtoEN(inp)    #translate french input to english
        
        #instantiates sentiment object
        s = sentiment(inp)
        #instantiates twitter object
        twit = twitter(inp)
        #determines if input is not a sentiment.
        if(s.isNotSentiment()):
            #Run every sentence with different synonym combinations till one is recognized
            sentence_list = synonym_sentences(inp)
            for inp in sentence_list:
                
                #results will hold the predicted value of the tags in corrispondence with the user's input    
                results = model.predict([l.bag_of_words(inp, words)])[0]
                #Grab the highest result and store it in results_index
                results_index = numpy.argmax(results)
                #Grab the tag belonging to the highest result
                global tag
                tag = labels[results_index]
                #Un-comment the code below to see the probability % of each tag that matches in results, and the tag that has the max probability.
                #print(results)
                #print(tag)

                #Check if the probability is higher than a set amount. We use 0.8 here to determine if we want to bot to give a random
                #response or for it to say "it didn't understand"
                if results[results_index] > 0.8:
                    for t in data["intents"]:
                        if t['tag'] == tag:
                            responses = t['responses']
                    if(isInFrench == True):
                        return trans.translateENtoFR(random.choice(responses))  #translate random response to French
                    else:
                        return random.choice(responses)
            global others
            others = ["I didn't quite understand", "I failed to understand what you were trying to say!", "Come again?", "Could you please repeat that for me?", "What language is that?"]
            if(isInFrench == True):
                return trans.translateENtoFR(random.choice(others)) #translate random response to French
            else:
                return random.choice(others)
        elif(inp.lower() == 'view recent tweet' or inp.lower() == 'see recent tweet'):   #if input is 'view recent tweet'
            return twit.retrieve_tweets()           #return the most recent tweet from Justin Trudeau
        else:
            #Determines sentiment value and returns appropriate response.
            sent = s.sentiment_analysis()
            if(isInFrench == True):
                return t.translateENtoFR(s.sentimentNumber(sent))   #translate sentiment response to French
            else:
                return s.sentimentNumber(sent)
    
