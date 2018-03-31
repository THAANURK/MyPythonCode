
# The Automatic customer review system.
# To satisfy customer review based on the previous data set.
# Author :  ShreeThaanu

from textblob import TextBlob
import csv

from textblob import Word
from textblob.wordnet import NOUN
from gtts import gTTS
import os
import nltk

from nltk.corpus import wordnet
import random

synonyms = []
antonyms = []

sentiment = ""
language = 'en'

def greet(yo):
    name = input("What's your name: ")
    return yo + name

print(greet("hi! "))

question = input("What's the query: ")
sentiment = TextBlob(question)

print("Sentiment Score: ", sentiment.sentiment.polarity)

writer = csv.writer(open("/Users/prasunsarkar/Desktop/ProducsData/Kurthi/kidstuffsbae.csv", 'a'))
writer.writerow([question])

if(sentiment.sentiment.polarity < 0):
    result = "sorry"
    print(result)

elif(sentiment.sentiment.polarity == 0):
    result = "idiot"
    print(result)

else:
 result = "great"
 print(result)

for syn in wordnet.synsets(result):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())
myRandomValue = random.choice(synonyms)
print(myRandomValue)

