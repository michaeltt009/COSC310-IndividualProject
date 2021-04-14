#This file controls the sentiment analysis of the user's input
#It will determine the level of sentiment of the user's input and return a statement based on the input
from pycorenlp import StanfordCoreNLP   #pycore used for Stanford's NLP toolkit

class sentiment:
    def __init__(self,inp):
        #takes in input of user
        self.inp = inp

    def isNotSentiment(self):
        #list of starting words in intents.json
        #used as statements/questions in intents.json do not have any sentiment
        startingWord = ["who", "what", "where", "when", "why", "how", "is", "do", 
                        "can", "what's", "hi", "hello", "whats", "good", "bye", 
                        "cya", "see", "goodbye", "have", "tell", "make", "are", 
                        "will", "which", "did"]
        #checks if the input starts with one of the starting words
        for word in startingWord:
            if self.inp.lower().startswith(word):
                return True
        return False

    def sentiment_analysis(self):
        #the StanfordCoreNLP server is running on http://127.0.0.1:9000
        nlp = StanfordCoreNLP('http://127.0.0.1:9000')
                # Json response of all the annotations
        output = nlp.annotate(self.inp, properties={
                "annotators": "tokenize,ssplit,parse,sentiment",
                "outputFormat": "json",
                # Only split the sentence at End Of Line. We assume that this method only takes in one single sentence.
                "ssplit.eolonly": "true",
                # Setting enforceRequirements to skip some annotators and make the process faster
                "enforceRequirements": "false"
                })
        # Only care about the result of the first sentence because we assume we only annotate a single sentence 
        return int(output['sentences'][0]['sentimentValue'])

    def sentimentNumber(self,sentiment):
        #determines level of sentiment
        #3 = good; 0 = bad
        if sentiment >= 3:
            return "Glad to hear you really like that."
        elif sentiment >= 2:
            return "I fully agree."
        elif sentiment >= 1:
            return "I can understand that."
        else:
            return "Sorry to hear that."
