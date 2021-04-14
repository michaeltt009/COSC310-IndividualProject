# COSC310-Interactive-Conversational-Agent
## Group 23

This project was done for COSC 310, and it's goal was to create an interactive conversational agent that would take in sentence input from the user and would output a response. The ChatBot we created is based on our current PM(as of 2020), Justin Trudeau, that will answer questions about his past, present and future.

This ChatBot implentation uses deeplearning through tensorflow's and tflearn's APIs. The basic idea is that through tensorflow, we will create a probabilistic function based on our input data (intents.json) and use this to estimate which "tag" most appropriately fits our user's input. Using this "tag" we can simply output a random hardcoded response. For example, if the user is to input "hello", the bot will calculate which tag is most fitting to the user's input. This will be returned as a float, representing a precentage from 0-100. The bot then simply take the MAX float and says that is the closest matching tag, and then grabs a random response belonging to the same tag. This is a good approach to the problem, as it allows the bot to work freely and not be constricted to handling only hardcoded inputs. 

The idea behind using tensorflow is that with a fullly interconnected neural network, passing data through it will give us a probablity gradient for each of our responses and their belonging tags.  Using something similar to a one-hot-encoded pattern, tensorflow works based an array of "zeros" in an array, representing all the words we have included in our expected inputs. When the user passes in a string, we increment at the index of the matching word in the array. Using this we can pass it through our nodes and pop out a response. 

### Downloading required APIs
> ```install nltk```  https://www.nltk.org/install.html
>
> ```install tensorflow``` https://www.tensorflow.org/install
>
> ```install tflearn``` http://tflearn.org/installation/
>
> ```install numpy``` https://numpy.org/install/
>

### Setting up
* Clone COSC310-Interactive-Conversational-Agent
* Open chat.py in your prefered python IDE
* In the terminal enter:
> ```import nltk```
> 
> ```nltk.download('punkt')```

### Running
* Compile and run chatbot.py


### Files
* **chatbot.py** *Has the actual chat function and calls ```load.py``` to create training data if none exists.*
* **load.py** *Loads in intents.json and processes the data into a trained tflearn model for a respons based on a probabilty of the corresponding tag to the question asked*
* **intents.json** *Database of tags, patterns, and responses.*
* **data.pickle** *Pickle file to store the processed files and not have to reprocesses them everytime*
* **model.tflearn** *tflearn models that have been stored as not to run the training algorithm everytime*
