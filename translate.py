#This file controls the translation of the user's input and the response from the bot
#It will translate the input and provide a translated version of the output
import google_trans_new  #google translate api
from google_trans_new import google_translator  #translator tool to translate strings

class translate:

    def __init__(self,inp):
        #takes in input of user
        self.inp = inp
        #Google Translate Object
        self.translator = google_translator()
    
    def detectFrench(self):
        #if language of input is in French
        if(self.translator.detect(self.inp)[0] == 'fr'):
            return True

    def translateFRtoEN(self,input):
        #return French input to English output
        return self.translator.translate(input, lang_src='fr', lang_tgt='en')
    
    def translateENtoFR(self,input):
        #return English input to French output
        return self.translator.translate(input, lang_src='en', lang_tgt='fr')
