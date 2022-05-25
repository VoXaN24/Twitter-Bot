import tweepy #Python Library for Twitter
import wget #Download img/vis
import datetime #uuuh it's time ?

def auth(conskey,conssecret,acctoken,acctokensecret): #Authentification
    auth = tweepy.OAuthHandler(conskey,conssecret)
    auth.set_access_token(acctoken,acctokensecret)
    return auth

def createapi(auth): #Create API Obj
    api = tweepy.api(auth)
    return api

def testauth(api): #Test Auth
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

def dlimg(url,file): #If u need to download the image or video
    wget.download(url,file)

def uploadmedia(medianame,api): #Upload Media
    media = api.media_upload(medianame)
    return media

def datetday(): #Take date and time
    date = datetime.datetime.now()
    return date

def madetweet(api,media,date): #Print a tweet with a img/vids and date and time
    tweet = "It's the %s/%s/%s at %s:%s:%s" % (date.day, date.month, date.year,date.hour, date.minute, date.second)
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

def madealistfromfile(): #It's in the name buddy
    a_file = open("url.txt", "r")
    list_of_lists = [(line.strip()).split() for line in a_file]
    a_file.close()

def main():
    #YES
    print('TO DO')