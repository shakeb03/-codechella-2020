import tweepy
auth =tweepy.OAuthHandler("aSi78YPjX9r7oyPJV6xcTuXoB","Uk36SGS8EHR8i2jzFKqy0ceEnNvVv9BK0rB0loQwsy3juoBP8Q")
auth.set_access_token("749544858013032448-qt2mB2XSWDxZHIOlEx1Og5ADTUDWiNB","cnoeyWfBmhrS1qCxuOdos7cUWGruC45Q1xklZvdFGninL")
api = tweepy.API(auth)
username= api.me()

followerslist=[]
followersImage=[]
followingslist=[]
followingsImage=[]
followers=api.followers(username.screen_name)
for follower in followers:
    followerslist.append(follower.screen_name)
    followersImage.append(follower.profile_image_url)
friends=api.friends(username.screen_name)
for friend in friends:
    followingslist.append(friend.screen_name)
    followingsImage.append(friend.profile_image_url)
print(followerslist)