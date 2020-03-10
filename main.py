from twython import Twython, TwythonStreamer
import threading
import database
from database import Tweet
from sqlalchemy.orm import sessionmaker,relationship
import datetime
import re


#Authentication Details
APP_KEY = "JyvKTUU98cMCIhhWC0MiMcwmZ"
APP_SECRET = "ZAgycA8nHsLf0KmGbjCm83Pvhe8vLX4C6dUy517Wfoe8GZJmKl"
OAUTH_TOKEN ="4218527549-kH6tulBQOtQIHjX8XFqPQZ32f72gBASpgebZYVi"
OAUTH_TOKEN_SECRET = "b7uD4wld9Lqv2fU59CBNZXJ1kHnbzK7PzE7BHaMPil25g"

#For Apeal
OAUTH_TOKEN = "900039071300321280-XNl26zmODa9cQ7TLnjj2HclzbKHyAtd"
OAUTH_TOKEN_SECRET = "qr5Ug6hpyWZOCabagdQRgu3Qx3cYUHIszIaPkdeamJDsj"

twitter = Twython(APP_KEY, APP_SECRET)

#File Location
filename = "./keywords.txt"


#Get Keywords Line By Line
lines = list(open(filename, 'r'))


#Convert date string to DateTime
def convert(date_time):
	format = '%a %b %d %H:%M:%S %z %Y'
	datetime_str = datetime.datetime.strptime(date_time, format)
	return datetime_str

#save tweet to database
def save_to_database(tweet, keyword):
	#initiate session with db
	Session = sessionmaker(bind=database.engine)
	session = Session()
	tweet_keyword = keyword
	tweet_possibly_sensitive = False
	tweet_created_at = tweet['created_at']
	tweet_created_at = convert(tweet_created_at)
	tweet_id = tweet['id_str']
	tweet_text = tweet['text']
	tweet_retweet_count = tweet['retweet_count']
	tweet_favorite_count = tweet['favorite_count']
	tweet_hashtags_used = []

	for hashtag in tweet['entities']['hashtags']:
		tweet_hashtags_used.append(hashtag['text'])


	tweet_symbols_used = []
	for symbol in tweet_symbols_used:
		tweet_symbols_used.append(symbol['text'])

	tweet_users_mentioned = []

	for user in tweet['entities'] ['user_mentions']:
		tweet_users_mentioned.append(user['screen_name'])

	tweet_user_screen_name = tweet['user']['screen_name']
	tweet_user_name = tweet['user']['name']
	tweet_user_verified = tweet['user']['verified']
	tweet_location = tweet['geo']

	if 'possibly_sensitive' in tweet:
		tweet_possibly_sensitive = tweet['possibly_sensitive']

	tweet_to_save = Tweet()
	tweet_to_save.tweet_created_at = tweet_created_at
	tweet_to_save.tweet_keyword = tweet_keyword
	tweet_to_save.tweet_id = tweet_id
	tweet_to_save.tweet_text = tweet_text
	tweet_to_save.tweet_retweet_count = tweet_retweet_count
	tweet_to_save.tweet_favorite_count = tweet_favorite_count
	tweet_to_save.tweet_hashtags_used = tweet_hashtags_used
	tweet_to_save.tweet_symbols_used = tweet_symbols_used
	tweet_to_save.tweet_users_mentioned = tweet_users_mentioned
	tweet_to_save.tweet_user_screen_name = tweet_user_screen_name
	tweet_to_save.tweet_user_name = tweet_user_name
	tweet_to_save.tweet_user_verified = tweet_user_verified
	tweet_to_save.tweet_location = str(tweet_location)
	tweet_to_save.tweet_possibly_sensitive = tweet_possibly_sensitive
	session.add(tweet_to_save)
	session.commit()
	session.close()






#Get Data One By One For Each Keyword
keywords = ""
keywords_array = []

today_date = datetime.date.today()

for keyword in lines:
	keyword = keyword.replace("\n", "")
	keyword = keyword.replace(" ","")
	keywords+=keyword + ","
	keywords_array.append(keyword)
	reached_final = False
	try:
		print("Getting Data For" +keyword)
		results = twitter.cursor(twitter.search, q=keyword,return_pages=True)
		for page in results:
			for result in page:
				tweet_created_at = convert(result['created_at']).date()
				if tweet_created_at == today_date:
					#print("It's today")
					save_to_database(result, keyword)

				else:
					reached_final = True
					#print("It's not today, Skipping...")

				if reached_final == True:
					break

			if reached_final:
				break

	except StopIteration:
		print("Successfully Got Data For: " +keyword)

	except Exception as e:
		print(str(e))
