import nltk
from nltk.corpus import wordnet as wn 
from pycorenlp import StanfordCoreNLP

# This function takes in the user's input sentence, assigns Part-of-Speech tags to each word, then places the nouns and verbs into a dictionary.
def pos_tag(sentence):

    # Set up the Stanford CoreNLP Server
    nlp = StanfordCoreNLP('http://localhost:9000')

    # Use the API to POS-tag the sentence and get a json file back as output
    output = nlp.annotate(sentence, properties = 
    {
        'annotators': 'pos',
        'outputFormat': 'json',
    })
    
    # dict_replacements will contain all important words that we will find synonyms for as values and the keys will be the POS tag.
    # If word matches the specified POS tag, add it to dict_replacements along with the correct POS tag recognized by wordnet.
    # Run a loop that iterates over each word in the sentence we take in as input.
    # POS-tags (CoreNLP - Stanford): NN - Noun(Singular), NNS - Noun(Plural), VB - Verb
    # POS-tags (Wordnet) = n - noun, v - verb
    dict_replacements = {}
    pos_list = []
    for sent in output['sentences']:
        for word in sent['tokens']:
            if word['pos'] == 'NNS' or word['pos'] == 'NN':
                dict_replacements[word['word']] = 'n'
                
    return dict_replacements            


# This method calls pos_tag() to get a dictionary containing replacement words and their POS-tag.
# This dictionary is then used to find synonyms and broader/more specific terms related to each word, 
# replace them with the original word in the sentence and add it to a sentences list
# Splits any compound words separated by hyphens.
# Returns the list of sentences (including user's input sentence) with key words replaced by different synonyms in each sentence.
def synonym_sentences(sentence):

    # Final sentence list has user's input as first sentence
    sentence_list = [sentence]

    #Get dictionary with word as key and POS-tag as value.
    dict_replacements = pos_tag(sentence)

    # If no useful words found, return list containing only user's initial input sentence.
    if not dict_replacements:
        return sentence_list
    
    # For each replacable word, find synsets. If they don't exist, return user's initial sentence.
    for word in dict_replacements.keys():
        syn = wn.synsets(word, dict_replacements.get(word))
        if syn is None:
            return sentence_list

        # For each synonym in the synset, find hypernyms(Broader-category words) and hyponyms(more specific words) and add them to their own lists.
        # If they dont exist, keep their lists empty to avoid crashes.
        for each_syn in syn:
            try:
                list_hypernyms = each_syn.hypernyms()
                list_hyponyms = each_syn.hyponyms()
            except:
                list_hypernyms = []
                list_hyponyms = []

            # list_newwords contains lists of hyper/hyponyms and words similar to them that we are going to use to replace the original words in the sentence.
            list_newwords = []
            for hyponym in list_hyponyms:
                list_newwords.append(hyponym.lemma_names())

            for hypernym in list_hypernyms:
                list_newwords.append(hypernym.lemma_names())
            # Replacing original sentence with new words and adding it to sentences_list
            for list in list_newwords:
                for newword in list:
                    if "_" in newword:
                        newword = newword.replace("_", " ")
                    sentence_list.append(sentence.replace(word, newword))

    # Return sentences_list containing many different sentences with different combinations of synonyms
    return sentence_list