# **COSC310 - Individual Project**

## **Group 23**

This project was created for COSC 310, and its goal is to create an interactive conversational agent that would take in sentence input from the user and would output an appropriate response. The ChatBot we created is based on the current Prime Minister of Canada, Justin Trudeau, who answers the user's questions based on his past, present, future and his relationships.

This ChatBot implentation uses deeplearning through tensorflow's and tflearn's APIs. The basic idea is that through tensorflow, we will create a probabilistic function based on our input data (intents.json) and use this to estimate which "tag" most appropriately fits our user's input. Using this "tag", we can simply output a random hardcoded response. For example, if the user is to input "hello", the bot will calculate which tag is most fitting to the user's input. This will be returned as a float, representing a precentage from 0-100. The bot then simply takes the MAX float and says that is the closest matching tag, and then grabs a random response belonging to the same tag, in this case the "greetings" tag. This is a good approach to the problem, as it allows the bot to work with fewer constraints and without handling only hardcoded inputs.

The idea behind using tensorflow is that with a fully inter-connected neural network, passing data through it will give us a probablity gradient for each of our responses and their belonging tags.  Using something similar to a one-hot-encoded pattern, tensorflow works based on an array of "0s", representing all the words we have included in our expected inputs. When the user passes in a string, we increment at the index of the matching word in this "0's" array to a "1". Using this we can pass it through our nodes and pop out a response.

We have also implemented some features to further enhance the user's experience and to improve the flow of conversation with the chat bot. A Graphical User Interfance(GUI) has been used in place of the terminal for input/output, so that the user has a more pleasant experience when talking with the bot. The bot also utilizes Stanford's CoreNLP Toolkit to make use of features such as Sentiment Analysis, which allows the bot to provide appropriate responses to statements that are not present in the question bank, and Part-of-speech(POS) tagging which helps the bot recognize certain key words as parts of speech(useful for performing other functions). Synonym recognition was also be implemented with the use of NLTK's WordNet. This feature helps the bot understand a wider range of vocabulary and sentences while providing the correct response.

For the individual project, I have implemented a Google Translate API and a Twitter API. The Google Translate API will assist in translating French input so that the chat bot can respond with an answer in French. The Twitter API will assist in retrieving the chat bot's most recent Tweet so that the user of the chat bot can view the text of the most recent Tweet by the chat bot.

## **Downloading required APIs**
> ```install nltk```  https://www.nltk.org/install.html
>
> ```install tensorflow``` https://www.tensorflow.org/install
>
> ```install tflearn``` http://tflearn.org/installation/
>
> ```install numpy``` https://numpy.org/install/
>
> ```install pycorenlp``` https://pypi.org/project/pycorenlp/
>

## **Newly added APIs**
> ```install google-trans-new```  https://pypi.org/project/google-trans-new/
>
> ```install tweepy``` https://docs.tweepy.org/en/latest/install.html
>

## **Setting up**
* Clone the COSC310-Interactive-Conversational-Agent repository
* Open ```chatbot.py``` in your prefered Python IDE
* In the terminal enter:
> ```import nltk```
> 
> ```nltk.download('punkt')```
>
> ```nltk.download('wordnet')```

* Download the Stanford NLP Toolkit (CoreNLP) zip folder https://stanfordnlp.github.io/CoreNLP/
* Extract the zip file to one directory level above this project's folder
> For example, if your project folder is located at 
> ```C:\Users\USER\COSC310-INTERACTIVE-CONVERSATIONAL-AGENT```, then extract file to ```C:\Users\USER\```


## **Running**
* Compile and run stanfordload.py
> If this does not work, run
> ```java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000```
> in the terminal where your Stanford NLP Toolkit unzipped folder is located.
* Compile and run gui.py


## **Files**
* **chatbot.py** *Has the chat function that returns bot's response to ```gui.py``` and calls ```load.py``` to create training data if none exists.*
* **load.py** *Loads in intents.json and processes the data into a trained tflearn model for a response based on a probabilty of the corresponding tag to the question asked*
* **intents.json** *Database of tags, patterns, and responses.*
* **data.pickle** *Pickle file to store the processed files and not have to reprocesses them everytime*
* **model.tflearn** *tflearn models that have been stored as not to run the training algorithm everytime*
* **stanfordload.py** *Establishes connection to Stanford's CoreNLP Server*
* **gui.py** *Comprises of functions that make the GUI for the chat bot*
* **sentiment.py** *Contains functions that conduct sentiment analysis on the user's input statement using Stanford's CoreNLP Toolkit*
* **syn_recognition.py** *Contains functions that tag parts-of-speech in user's input, and creates different sentences with different combinations of synonyms*
* **test_chatbot.py** *Contains unit tests for major functions and classes to validate them*

## **Newly added API files**
* **translate.py** *Translates input and responses from english to french and from french to enlish*
* **twitter.py** *Receives most recent tweet from chat bot person*


## **List of Old Features**

### 1. Graphical User Interface(GUI)
A simple GUI was implemented to provide a much more appealing way of using the chat bot. This GUI was made using Tkinter and image functionalities from Pillow were utilized. It consists of a medium-sized window with a text box(to display the conversation), an entry box(for the user to type their message in), a 'Send' button which can be pressed to send the typed message to the bot(They can also choose to press 'Enter'), and various other smaller features such as a label containing the image and name of the person who the bot is based on, and a scrollbar for the user to access/read older sections of the conversation. Here is an image showcasing the GUI with a few turns of conversation:

![GUI](/images/GUI_sample.PNG)

### 2. Part-of-Speech(POS) Tagging
Stanford's CoreNLP Toolkit is used to tokenize and categorize each word in the user's input sentence to specific parts of speech. If the word's POS matches with the one specified, it is placed into a dictionary of words that would be later used for another feature. The values assigned to each word is their corresponding POS, which is converted from Stanford's CoreNLP format to NLTK.WordNet's format. Here is an image displaying sample output for a possible sentence that the user could input, and its breakdown into different parts of speech, along with the dictionary of key words(Note: The following output is not visible in the final version of the application. This image is for demonstration purposes only):

![POS](/images/POS_sample.PNG)

### 3. Synonym Recognition
A lexical database in the form of NLTK's WordNet is used to find synonyms of key words from the user's input sentence(see above feature on how to get these 'key words'). The original word is then replaced by each of these synonyms to form a new sentence, each of which is stored in a list. This list is returned to ```chatbot.py``` where each sentences in incrementally sent to the bot until it recognizes one and forms an appropriate response. If none of the sentences manage to get recognized, an appropriate message from the bot is shown to the user instead(Note: The first sentence in the list is always the user's original input). The following image showcases the bot's ability to recognize different words as synonyms of each other and provide the same type of response to all sentences:

![SYN](/images/SYN_sample.PNG)

### 4. Sentiment Analysis
The CoreNLP Toolkit is also used to perform Sentiment Analysis; it detects words in the sentence that have different levels of sentiment and provides an integer value from 0-3 based on how positive or negative the sentiment is. The bot then responds appropriately based on the sentiment number generated from the sentence. Here is a sample image of the bot responding to different levels of sentiment with the user's input sentences:

![SENT](/images/SENT_sample.PNG)

### 5. Extra Topic of Conversation
The bot now supports conversation about his father, Pierre Trudeau and his relationship with him. The following image demonstrates some new possible combinations of dialogue with the bot:

![CONV](/images/CONV_sample.PNG)

### 6. Varied 'Fail' Responses
When the bot fails to recognize a sentence input by the user, it now has the possibility to reply with 5 different responses instead of just one. The image below showcases this new feature:

![FAIL](/images/FAIL_sample.PNG)

### Spelling Error Detection
The Lancaster Stemmer Algorithm tokenizes the words in the user's input sentence, stems them to provide the root words, removes 'stop words' and as a result, can handle minor spelling errors. The following image shows the bot's ability to respond appropriately even if the input sentence has minor errors in spelling:

![SPELL](/images/SPELL_sample.PNG)
