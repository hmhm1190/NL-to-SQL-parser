import nltk
from nltk.tokenize import (TreebankWordTokenizer,
                           word_tokenize,
                           wordpunct_tokenize,
                           TweetTokenizer,
                           MWETokenizer)

# Define the input question
question = "Show the names of singers with highest value in descending order of highest."

print(type(wordpunct_tokenize(question)[0]))