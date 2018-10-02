### Text Summarization ###

## Importing the Libraries ##
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

## Importing the dataset ##
dataset = open("President Speech.txt").read()

## Create the Function ##

def summarization(dataset):
    
    result = []
    for number, sentence in enumerate(sent_tokenize(dataset)):
        number_tokens = len(word_tokenize(sentence))
        tagged = nltk.pos_tag(word_tokenize(sentence))
        number_nouns= len([word for word, pos in tagged if pos in ["NN", "NNP"]])
        ners=nltk.ne_chunk(nltk.pos_tag(word_tokenize(sentence)), binary=False)
        number_ners=len([chunk for chunk in ners if hasattr(chunk,'label')])
        score=(number_ners + number_nouns) / float(number_tokens)
        result.append((number, score, sentence))
    return result

summ = summarization(dataset)
summ

## Print the Summary ##
for i in sorted(summ, key=lambda x: x[1], reverse=True):
    print(i[2])