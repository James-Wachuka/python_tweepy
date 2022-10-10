import get_twitter_api
import pandas as pd


api= get_twitter_api.twitter_api()

friends = api.friends_ids(api.me().id)
followers = api.followers_ids(api.me().id)
# function to followback your friends
def follow_back():
    to_follow=[]
    print("-------retrieving twitter information------")
    print("----------People you follow:---------\n", len(friends))
    print("---------Your Followers:---------\n", len(followers))
    for follower in followers:
        if follower not in friends:
            to_follow.append(follower)
            #api.create_friendship(follower)
    print("-----You have followed:",len(to_follow),"More----")

follow_back()


# function to get screennames

def get_follower_names(followers):
    follower__=[]
    for follower in followers:
        follower_=api.get_user(follower)
        follower__.append(follower_.screen_name)
    return follower__

def get_friend_names(friends):
    friend__=[]
    for friend in friends:
        friend_=api.get_user(friend)
        friend__.append(friend_.screen_name)
    return friend__

foll = get_follower_names(followers)
frie = get_friend_names(friends)
# create a df of follower names and friend names
df = pd.DataFrame(list(zip(foll, frie)),
               columns =['Friends', 'followers'])
print(df)


