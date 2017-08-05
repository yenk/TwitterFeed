'''''''''''''''''''''
TWEET ANALYSIS
'''''''''''''''''''''


#read json data from file, tweetdump.py into the same dictionary 
import datetime 
import json
import matplotlib.pyplot as plt


#read json dataset
with open('realDonaldTrump_tweets.json') as json_intweets_file: 
#loads into a dictionary
  data_loaded = json.load(json_intweets_file)

#initial dictionary creation
# stupidtweets = data_loaded['tweets']

# #output entire stupidtweets dataset using python datetime now 
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

#print stupidtweets 

#compute count of tweets by year
def yearcount(stupidtweets): 
  #itinerate each tweet and get year first, then increment count, dict 
  yearcount ={}
  for t in stupidtweets: 
    year = t['created'].year

    if year in yearcount: 
      yearcount[year] += 1
    else: 
      yearcount[year] = 1  
  return yearcount
  
# print yearcount(stupidtweets)  

# #compute count of tweets by month 
def monthcount(stupidtweets): 
  monthcount = {}
  for t in stupidtweets: 
    month = t['created'].month

    if month in monthcount: 
      monthcount[month] += 1
    else: 
      monthcount[month] = 1
  return monthcount

# print monthcount(stupidtweets)

#compute tweet counts by week 
def weekcount(stupidtweets): 
  week_count = {}
  for t in stupidtweets: 
    #isocalendar is a tuple that returns year/week/day count
    #accessing the tuple's week element would be [1], e.g. (2016, 50, 3)
    dayofweek = t['created'].isocalendar()[1] 

    if dayofweek in week_count: 
        week_count[dayofweek] += 1
    else: 
        week_count[dayofweek] = 1
  return week_count

# print weekcount(stupidtweets)

# compute tweet counts by day
def daycount(stupidtweets): 
  daycount = {}
  for t in stupidtweets: 
    day = t['created'].day

    if day in daycount: 
      daycount[day] += 1
    else: 
      daycount[day] = 1
  return daycount

# print daycount(stupidtweets)

#compute tweet counts for each day of the week
def daycount(stupidtweets): 
  datecount = {}
  for t in stupidtweets:
    # date = t['created'].timetuple()
    date = t['created'].weekday() 

    if date in datecount: 
      datecount[date] += 1
    else: 
      datecount[date] = 1
  return datecount 

# print daycount(stupidtweets)
#output: {0: 470, 1: 523, 2: 494, 3: 521, 4: 456, 5: 404, 6: 374}


#create a function to output name of the day, e.g. monday = 1, output monday 
def dayname(daycount): 
  #create name of day, to be referenced in dictionary via key variable, must match index of weekday
  day_name = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  dict_day_name = {}
  for key, value in daycount.items(): 
    # print day_name[key]
    dict_day_name[day_name[key]] = value 

  return dict_day_name

# print dayname(daycount(stupidtweets))

#output: {'Monday': 470, 'Tuesday': 523, 'Friday': 456, 'Wednesday': 494, 'Thursday': 521, 'Sunday': 374, 'Saturday': 404}

'''''''''''''''''''''
TWEET PLOTTING
'''''''''''''''''''''

#create histogram of the daycount in matplot  

def histogram_plot(dayname): #remember to call parameter name, easier to reference previous method after you defined it
  #use bar chart function instead of histogram 
  centers = range(len(dayname))

  font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

  plt.bar(centers, dayname.values(), align='center', tick_label=dayname.keys())
  plt.xlim([0, 20])
  # ax.set_title('total count of tweets per day') 
  # ax.set_xticks(ind_width) 
  # ax.set_xticklabels(labels_lst, rotation='vertical', fontsize=6)
  plt.xlabel('tweets per day', fontdict=font)
  plt.ylabel('count of tweets', fontdict=font)
  # plt.subplots_adjust(top=.2, bottom=0.2) #adjust x/y labeling
  plt.show()


histogram_plot(dayname(daycount(stupidtweets)))


# #compute the total number of tweets 
def count(stupidtweets): 
  return len(stupidtweets)

# print 'total stupid tweets count is:', count(stupidtweets)

# # write a method(function) to convert json string date to an actual python date
def date_conversion(str): 
  return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
# print date_conversion('2017-07-28 16:13:21')

# d = date_conversion('2017-07-28 16:13:21')

# print 'year:', d.year
# print 'month:', d.month
# print 'day:', d.day
# print 'hour:', d.hour



# # print tweets_date_conversion('2017-07-28 16:13:21')
