'''
This script will first load latest 100 twitter feeds from today to last loaded date.

Then will continue loading from last loaded date to next oldest date in a while loop until it's completely zero'd out. 

Then gets output into a json data type. 

'''

import tweepy #https://github.com/tweepy/tweepy
# import csv
import json

'''
Twitter API credentialing process: 

1. create a twitter user login account
2. use login account to log into https://apps.twitter.com/ to obtain API credentials
3. twitter will generate an authenticated security keys (consumer and access keys) to retrieve 
twitter data through its API. 

'''

#twitter API credentialing

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#Twitter only allows access to a users most recent 3240 tweets with this method
def get_all_tweets(screen_name):
  
  #authorize twitter, initialize tweepy
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)
  
  #initialize a list to hold all the tweepy Tweets
  alltweets = []  
  
  #make initial request for most recent tweets (200 is the maximum allowed count)
  new_tweets = api.user_timeline(screen_name = 'realDonaldTrump',count=100)
  
  #save most recent tweets
  alltweets.extend(new_tweets)
  
  #save the id of the oldest tweet less one
  oldest = alltweets[-1].id - 1
  
  #keep grabbing tweets until there are no tweets left to grab
  while len(new_tweets) > 0:
    print "getting tweets before %s" % (oldest)
    
    #all subsequent requests use the max_id param to prevent duplicates
    #append this oldest 100 records to the last "dated" current alltweets 
    new_tweets = api.user_timeline(screen_name = 'realDonaldTrump',count=100,max_id=oldest)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #update the id of the oldest tweet from the last retrieved tweets
    oldest = alltweets[-1].id - 1
    
    print "...%s tweets downloaded..." % (len(alltweets))
  
  #transform the tweepy tweets into a 2D array to create the csv file
  # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
  
  # #write the csv  
  # with open('%s_tweets.csv' % screen_name, 'wb') as f:
  #   writer = csv.writer(f)
  #   writer.writerow(["id","created","text"])
  #   writer.writerows(outtweets)

  #writing json data into a dictionary in a for loop, appending alltweets to outweets. 
  outtweets = {} 

  outtweets['tweets'] = [] 

  for t in alltweets:
    outtweets['tweets'].append({
     'id': t.id_str, 
     'created': t.created_at,
     'text': t.text.encode('utf-8')})


  #write to json
  with open('%s_tweets.json' % screen_name, 'wb') as f:
    #default=str converts datetime format to a string for 'created' date variable 
    json.dump(outtweets, f, default=str)  

  
  pass

#this is necessary to run/import modules 
if __name__ == '__main__':
  #pass in the username of the account you want to download
  #this basically retrieves everything corresponding to this username e.g. #realDonalTrump
  get_all_tweets("realDonaldTrump") 