import tweepy #Python Library for Twitter
import wget

def auth(conskey,conssecret,acctoken,acctokensecret): #Authentification
    auth = tweepy.OAuthHandler(conskey,conssecret)
    auth.set_access_token(acctoken,acctokensecret)
    return auth

def createapi(auth): #Create API Obj
    api = tweepy.api(auth)
    return api

def dlimg(url): #If u need to download the image or video
    wget.download(url,file)

