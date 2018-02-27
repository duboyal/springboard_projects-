import tweepy
import json
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from nltk.tokenize import TweetTokenizer

from collections import Counter


nltk.download('punkt')

#tt = TweetTokenizer()

# String of path to file: tweets_data_path
tweets_data_path = 'tweetsETH2.txt'
tweets_data_path2 = 'tweetsETH.txt'
tweets_data_path3 = 'tweetsETH3.txt'
tweets_data_path4 = 'tweetsETH4.txt'
tweets_data_path5 = 'tweetsETH5.txt'
tweets_data_path6 = 'tweetsETH6.txt'
tweets_data_path7 = 'tweetsETH7.txt'
tweets_data_path8 = 'tweetsETH8.txt'
tweets_data_path9 = 'tweetsETH9.txt'
tweets_data_path10 = 'tweetsETH10.txt'
tweets_data_path11 = 'tweetsETH11.txt'

tweets_data_path14 = 'tweetsETH14.txt'
tweets_data_path15 = 'tweetsETH15.txt'
tweets_data_path16 = 'tweetsETH16.txt'
tweets_data_path17 = 'tweetsETH17.txt'



# Initialize empty list to store tweets: tweets_data
tweets_data = []
#APPEND TO SAME EMPTY LIST

# Open connection to file 1
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#------
# Open connection to file 2
tweets_file = open(tweets_data_path2, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame

#---------
# Open connection to file 3
tweets_file = open(tweets_data_path3, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame

#---------
# Open connection to file 4
tweets_file = open(tweets_data_path4, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 5
tweets_file = open(tweets_data_path5, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 6
tweets_file = open(tweets_data_path6, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 7
tweets_file = open(tweets_data_path7, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 8
tweets_file = open(tweets_data_path8, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 9
tweets_file = open(tweets_data_path9, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 10
tweets_file = open(tweets_data_path10, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame
#---------
# Open connection to file 11
tweets_file = open(tweets_data_path11, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame




#---------
# Open connection to file 14
tweets_file = open(tweets_data_path14, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame

#---------
# Open connection to file 15
tweets_file = open(tweets_data_path15, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame

#---------
# Open connection to file 16
tweets_file = open(tweets_data_path16, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame

#---------
# Open connection to file 17
tweets_file = open(tweets_data_path17, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
#tweets data is a list and you can put that into a data frame



#--------
# Build DataFrame of tweet texts and languages
#df = pd.DataFrame(tweets_data)
#print(list(my_dataframe.columns.values))
#print("---------")

df = pd.DataFrame(tweets_data, columns= ['text', 'lang'])

print(list(df.columns.values))

# Print head of DataFrame
print(df.head())
print("--------------")
print(df['text'])
print("-----")
print(len(df))

#df['tokenized_text'] = df['text'].apply(word_tokenize)

#print("row of")

tt = TweetTokenizer()

df['tokenized_sents'] = df['text'].apply(tt.tokenize)

print(df['tokenized_sents'])


TokenList = []


print("this")
#this was a list of lists

for row in df['tokenized_sents']:
    for i in row:
        TokenList.append(i)

print("--here we are--")
#print(TokenList)

token_lower = [t.lower() for t in TokenList]

print(token_lower)

#----

print("HERE WE ARE")
bow_simple = Counter(token_lower)

print(bow_simple.most_common(30))
