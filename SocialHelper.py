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

def printFollowingRatio():
    profile
    ratio = numFollowers/numFollowees
    if(ratio<.5):
        print("Here's your ratio: ", ratio)
        print("Grade: B-")
        print("Strong start! Keep working at it!")
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

def getFollowingRatioGrade():
    if(ratio<.5):
        return "B-"
    elif(ratio<.8):
       return "B"
    elif(ratio<1):
       return "B+"
    elif(ratio<1.2): 
        return "A-"
    elif(ratio<2):
       return "A"
    elif(ratio>=2):
       return "A+"

def getFollowingRatio():
    return numFollowers/numFollowees

def getLikesRatio():
   if(profile.mediacount >= 3):
        sum = 0
        mostRecentPost = next(posts)
        sum += mostRecentPost.get_likes
        secondMostRecentPost = next(posts)
        sum += secondMostRecentPost.get_likes
        thirdMostRecentPost = next(posts)
        sum += thirdMostRecentPost.get_likes
        return sum/3/numFollowers
   elif(profile.mediacount == 2):
        sum = 0
        mostRecentPost = next(posts)
        sum += mostRecentPost.get_likes
        secondMostRecentPost = next(posts)
        sum += secondMostRecentPost.get_likes
        return sum/2/numFollowers
   elif(profile.mediacount == 1):
        sum = 0
        mostRecentPost = next(posts)
        sum += mostRecentPost.get_likes
        return sum/numFollowers
   else: 
        return 0

def getLikesRatioGrade():
    if(getLikesRatio()<.1):
        return "B-"
    elif(getLikesRatio()<.2):
        return "B"
    elif(getLikesRatio() <.333):
        return "B+"
    elif(getLikesRatio() <.5):
        return "A-"
    elif(getLikesRatio() < 1):
        return "A"
    else:
        return "A+"

def printLikesRatio():
    ratio = getLikesRatioGrade()
    if(getLikesRatioGrade() != "A+"):
        print("In general, most of the time people get less likes on a post than followers they have. This is a very normal occurence and should not be seen as a bad thing.")
        if(getLikesRatioGrade() == "B-"):
            print("Here's your ratio: ", ratio, " B- This isn't a terrible spot to be in. Your likes ratio may be a little low, but that's ok! The only way to go is up!") 
        elif(getLikesRatioGrade() == "B"):
            print("Here's your ratio: ", ratio)
            print("Grade: B")
            print("This is a strong start. This number indicates that you have a modest loyal fanbase.")
        elif(getLikesRatioGrade() == "B+"):
            print("Here's your ratio: ", ratio)
            print("Grade: B+")
            print("This is a great spot to be in! A B+ is a strong score, and it shows that a large amount of your followers like your posts. Keep it up!")
        elif(getLikesRatioGrade() == "A-"):
            print("Here's you ratio: ", ratio)
            print("Grade: A-")
            print("Wow! This is amazing! Over a third of your followers have likes your last three posts! This is an ideal place to be in! Keep it up!")
        elif(getLikesRatioGrade() == "A"):
            print("Here's your ratio: ", ratio)
            print("Grade: A")
            print("This is amazing! Over half of your followers have liked your last three posts! You have a large and loyal dedicated fanbase. Nice work and keep on posting!")
    else: 
        print("Here's your ratio: ", ratio)
        print("Grade: A+")
        print("This is amazing! Consistently having more likes than followers is something to be proud of! You're either famous, a local celebrity, or just someone special! Your fanbase is large and loyal, along with some secret followers who may not be actually be following you. Nice job and keep it up!")
        
def getCommentToLikesRatio():
    if(profile.mediacount >= 3):
        sum = 0
        mostRecentPost = next(posts)
        sum += mostRecentPost.get_comments



print(posts.get_comments())
