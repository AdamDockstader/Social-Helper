import instaloader
import pandas as pd
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'adamdockstaderr')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)

numFollowers = profile.followers
numFollowees = profile.followees
posts = profile.get_posts()

def getFollowingRatio():
    profile
    ratio = numFollowers/numFollowees
    if(ratio<.5):
        print("Here's your ratio: ", ratio, ". B- Strong start! Keep working at it!")
    elif(ratio<.8):
        print("Here's your ratio: ", ratio, " B This is a good spot to be in. Your ratio is pretty good.")
    elif(ratio<1):
        print("Here's your ratio: ", ratio, " B+ Nice job! Having a ratio this close to 1 is very solid. Keep it up!")
    elif(ratio<1.2): 
        print("Here's your ratio: ", ratio,  "A- Wow! Great job! You have a positive ratio. You are at the first step to being insta famous!")
    elif(ratio<2):
        print("Here's your ratio: ", ratio, " A This is great! You solidly have more followers than following. This is a great account!")
    elif(ratio>=2):
        print("Here's your ratio: ", ratio, " A+ You've done it! You have a perfect ratio!")

def getLikesRatio:
   if(profile.mediacount >= 3):
        sum = 0
        mostRecentPost = next(posts)
        






