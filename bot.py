import tweepy #Python Library for Twitter
import wget
import datetime

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

def uploadimg(imgname,api): #Upload IMG
    img = api.media_upload(imgname)
    return img

def uploadvids(vidsname,api): #Upload VIDS
    vids = api.media_upload(vids)
    return vids

def datetday(): #Take date and time
    date = datetime.datetime.now()
    return date

def madetweet(api,media,date): #Print a tweet with a img/vids and date and time
    tweet = "It's the %s/%s/%s at %s:%s:%s" % (date.day, date.month, date.year,date.hour, date.minute, date.second)
