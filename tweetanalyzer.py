'''
read json data from file, tweetdump.py into the same dictionary 
'''
import datetime 
import json


#read json data 
with open('realDonaldTrump_tweets.json') as json_intweets_file: 
#loads into a dictionary
  data_loaded = json.load(json_intweets_file)

#initial dictionary creation
# stupidtweets = data_loaded['tweets']

#output entire stupidtweets dataset using python datetime now 
def tweets_date_conversion(tweets): 
  for i in range(len(tweets)): 
    t = tweets[i]
    #convert date into 'stupidtweets' dict with new 'created' python date 
    newdate = datetime.datetime.strptime(t['created'], '%Y-%m-%d %H:%M:%S')
    #assigning a new converted date to old created date
    t['created'] = newdate 
    tweets[i] = t
  return tweets

# #converting json date from stupidtweets dictionary, via function call (tweets_date_conversion)
stupidtweets = tweets_date_conversion(data_loaded['tweets'])

# print stupidtweets 

#compute count and tweet for each year



# # compute the total number of tweets 
def count(stupidtweets): 
  return len(stupidtweets)

print 'total stupid tweets count is:', count(stupidtweets)

# write a method(function) to convert json string date to an actual python date
def date_conversion(str): 
  return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
# print date_conversion('2017-07-28 16:13:21')

d = date_conversion('2017-07-28 16:13:21')

print 'year:', d.year
print 'month:', d.month
print 'day:', d.day
print 'hour:', d.hour



# # print tweets_date_conversion('2017-07-28 16:13:21')
