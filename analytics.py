import tweepy					# Python twitter API package
import unidecode		# for processing text fields in the search results
import datetime

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "3kefI1xfIBc1jlS8PsQCjqwts"
CONSUMER_KEY_SECRET = "Wbb8850WLT1oIt5m3IIEZFClGh5DWLpcA7FzBlCV3zPl2ckvEf"
ACCESS_TOKEN = "1183569034933084160-MLPbysT18wzMYsuKkFm53h6GxiNgvn"
ACCESS_TOKEN_SECRET = "l2vDzhuGO0RrFSENng5HvcxdIbrGLBgi5Lp0nENiCMFOM"

#API Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  using wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)


search_terms = "catalinmpit"

t_id = api.get_user(search_terms).id
t_un = api.get_user(search_terms).name
t_sn = api.get_user(search_terms).screen_name
t_desc = api.get_user(search_terms).description
t_fc = api.get_user(search_terms).followers_count

def twitter_search(search_terms):
# Get Information About a Twitter User Account
        startDate = datetime.datetime(2020,11,14, 0,0,0)
        # print(startDate)
        endDate = datetime.datetime(2020, 11, 21, 0,0,0)
        # print(endDate)
        tweets =[]
        # for tweet in tmptweets:

        twitter_user = api.get_user(search_terms)
        # statuses = api.mentions_timeline() 
        # print("TOTAL MENTIONs COUNT",str(len(statuses)))
        # followers_count = twitter_user.followers_count
        # print("FOLLOWERS COUNT",followers_count)
        # tweets_count = twitter_user.statuses_count 
        # print("TWEETS COUNT",tweets_count)
        # n = api.user_timeline(id=twitter_user.id, since_id=startDate, max_id= endDate)
        # print("since date count tweet",len(n))
        # for i in n:
        #   print("printing text",unidecode.unidecode(i.text))
        if twitter_user:
        # Get Basic Account Information
            print("twitter_user id: ", twitter_user.id)
            print("twitter_user name: ", twitter_user.name)
            print("twitter_user screen name: ", twitter_user.screen_name)
            print("twitter_user description: ", twitter_user.description)
            print("twitter_user Followers count: ", twitter_user.followers_count)

            tmpTweets = api.user_timeline(id=twitter_user.id)
            m = api.user_timeline(id=twitter_user.id, count=10)
            #print(m)
            for i in range(len(m)):
              texts = m[i].text
              text = unidecode.unidecode(texts)
              #print("twitter_user latest tweet: ", text)
              #print("Retweet Count",m[i].retweet_count)
              #print("Fav count", m[i].favorite_count)
            #new_tweets = api.user_timeline(screen_name=twitter_user.screen_name, count=1)
            #check if tweet are available for display
            if tmpTweets:
                #get the most recent tweet by the user
                n = api.user_timeline(id=twitter_user.id, count=1)[0]
                #text = n.text
                texts = n.text
                  # text = unidecode.unidecode(texts)
                  # print("twitter_user latest tweet: ", text)
                  # print("Retweet Count",n.retweet_count)
                  # print("Fav count", n.favorite_count)
                  # text of the tweet
                text = unidecode.unidecode(texts)
                print("twitter_user latest tweet: ", text)
            else:
                print("No tweets by the user")
            #get tp n followers
           # print("Top 10 followers screen name as follows:")
            #print('')
            follow = api.followers_ids(id=twitter_user.id, count=10)[0:10]
            #display if exists
            if len(follow) > 0:
                #print(follow)
             #   print("Printing followers ", len(follow))
                for i in follow:
                    screen = api.get_user(id=i)
                print("Follower Screen name ", screen.screen_name)
            else:
                print("No followers", len(follow))
            #u = raw_input("Wish to continue? Enter user name")
           # if u == "STOP":
                exit()
           # else:
            #    twitter_search(u)
            tmpTweets = api.user_timeline(id=twitter_user.id)
            #print("tmptweets",tmpTweets)
            statuses = api.mentions_timeline(since_id=startDate,max_id=endDate)
            status=api.mentions_timeline()
            print("TOTAL MENTIONs in 7 days",str(len(statuses)))
            print("TOTAL MENTIONs COUNT",str(len(status)))
            followers_count = twitter_user.followers_count
            print("TOTAL FOLLOWERS COUNT",followers_count)
            # c=tweepy.Cursor(api.followers, twitter_user,since=startDate,max_id=endDate,until=endDate)
            # for t in tweepy.Cursor(api.followers, twitter_user,since=startDate,max_id=endDate,until=endDate).items():
            #   print(t.followers_count)
            
            # for follower in tweepy.Cursor(api.followers, twitter_user):

            tweets_count = twitter_user.statuses_count 
            print("TWEETS COUNT",tweets_count)
            for twwet in tmpTweets:
              if twwet.created_at < endDate and  twwet.created_at > startDate:
                tweets.append(twwet)
            
            print("TWEETS in 7 Days ",len(tweets))

#Prompt user to enter screen name

#STOP if no longer wish to continue
if search_terms == "STOP":
    exit()
else:
    twitter_search(search_terms)
## code to get the followers and following of a user and store it in lists. We can find out the coommon elements and then they would be our followers who are follwoing you.
# auth =tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)
# username= api.me()
# followerslist=[]
# followingslist=[]
# followers=api.followers(username.screen_name)
# for follower in followers:
#     followerslist.append(follower)
# friends=api.friends(username.screen_name)
# for friend in friends:
#     followingslist.append(friends.screen_name)