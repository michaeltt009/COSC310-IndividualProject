#Unit Testing
import unittest
import chatbot
from load import load

class TestChatbot(unittest.TestCase):
    
    def setUp(self):
        self.l = load("intents.json")
        self.data = self.l.getData()
        for t in self.data["intents"]:
            if t['tag'] == "greeting":
                self.responses = t['responses']
            if t["tag"] =="music":
                self.responsesmusic = t['responses']
        #pass

    def tearDown(self):
        pass

    def test_chat(self):                
        self.assertTrue(chatbot.chat("How are you") in self.responses)
        self.assertTrue(chatbot.chat("Is anyone there?") in self.responses)
        self.assertTrue(chatbot.chat("hello") in self.responses)
        self.assertTrue(chatbot.chat("good day") in self.responses)
        self.assertTrue(chatbot.chat("whats up?") in self.responses)
               
    
    def test_tag(self):
        chatbot.chat("How are you")
        self.assertEqual(chatbot.tag,"greeting")
        chatbot.chat("see you later")
        self.assertEqual(chatbot.tag,"goodbye")
        chatbot.chat("how old")
        self.assertEqual(chatbot.tag,"age")

    def test_sentiment(self):
        self.assertEqual(chatbot.chat("I love your work"),"Glad to hear you really like that.")
        self.assertEqual(chatbot.chat("I hate you"),"I can understand that.")
        self.assertEqual(chatbot.chat("I like this conversation"),"I fully agree.")

    def test_capitalization(self):
        self.assertTrue(chatbot.chat("hOW aRE yOU") in self.responses)
        self.assertTrue(chatbot.chat("HOW ARE YOU") in self.responses)
        self.assertTrue(chatbot.chat("how are you") in self.responses)

    def test_punctuation(self):
        self.assertTrue(chatbot.chat("how are you.") in self.responses)
        self.assertTrue(chatbot.chat("how are you!") in self.responses)
        self.assertTrue(chatbot.chat("how are you?") in self.responses)

    def test_synonyms(self):
        self.assertTrue(chatbot.chat("what type of music do you listen to") in self.responsesmusic)
        self.assertTrue(chatbot.chat("what tunes do you listen to") in self.responsesmusic)
        

    def test_failResponses(self):
        self.assertTrue(chatbot.chat("Who is Gahlran?") in chatbot.others)
        self.assertTrue(chatbot.chat("do you play among us?") in chatbot.others)


if __name__ == '__main__':
    unittest.main()