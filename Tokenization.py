## Tokenization ##

# Importing the library
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Importing the Data
dataset = """Hello Mr. Watson, how are you doing today?
             The weather is awsome. The garden is green.
             We should go out for a walk."""
             
# Tokenize the Sentences
print(sent_tokenize(dataset))

for i in sent_tokenize(dataset):
    print(i)
    
# Tokenize the Words
print(word_tokenize(dataset))

for i in word_tokenize(dataset):
    print(i)
