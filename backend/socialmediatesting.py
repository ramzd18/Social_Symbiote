from twitter import user_lookup
from twitter import user_tweets
from reddit import redditapi
from reddit import redditusers
import re





# userid= user_lookup.find_user("sararecruiting")
# likedtweets=user_tweets.main(userid,"liked_tweets",10)
# tweets=user_tweets.main(userid,"tweets",20)
# # mentions=user_tweets.main(userid,"mentions",6)
# print(user_tweets.clean_tweets(tweets))
# print(user_tweets.clean_likedtweets(likedtweets))
# # print(user_tweets.clean_mentiontweets(mentions))

interestslist=['collecting antiques', 'exercise', 'sweepstakes', 'home improvement', 'reading', 'sports', 'the arts', 'hockey', 'watching hockey', 'home decoration', 'health', 'watching sports', 'photograph', 'cooking', 'cruises', 'outdoors', 'electronics', 'crafts', 'fitness', 'music', 'camping', 'dogs', 'movies', 'collecting', 'kids', 'medicine', 'diet', 'cats', 'travel', 'wine', 'motorcycling', 'investing', 'traveling', 'self improvement']
subredditslist= redditusers.get_commmon_subreddit(interestslist)
user= redditusers.get_users(interestslist,subredditslist)

comments= user[1]
username=user[0]
# print("hereherhehrer")
# print(redditusers.match_comments_with_titles(username,comments,"Sara"))




