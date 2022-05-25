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

def dlimg(url,file): #If u need to download the image or video
    wget.download(url,file)

def uploadimg(imgname,api,img):
    img = api.media_upload(imgname)
    return img

def uploadvids(vidsname,api,vids):
    vids = api.media_upload(vids)
    return vids

