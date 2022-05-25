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

def dlmedia(url,file): #If u need to download the image or video
    wget.download(url,file)
    printf("File Donwloaded")

def uploadmedia(medianame,api): #Upload Media
    media = api.media_upload(medianame)
    return media

def datetday(): #Take date and time
    date = datetime.datetime.now()
    return date

def madetweet(api,media,date): #Print a tweet with a img/vids and date and time
    tweet = "It's the %s/%s/%s at %s:%s:%s" % (date.day, date.month, date.year,date.hour, date.minute, date.second)
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    return post_result

def madealistfromfile(): #It's in the name buddy
    a_file = open("url.txt", "r")
    list = [(line.strip()).split() for line in a_file]
    a_file.close()
    return list

def verifvalue(conskey,conssecret,acctoken,acctokensecret): #Verif if empty
    a = 0
    if conskey == "" :
        print("Please the your Consumer Key")
        a = 1
    if conssecret == "":
        print("Please set your Consumer Secret Key")
        a = 1
    if acctoken == "" :
        print("Please set your Access Token Key")
        a = 1
    if acctokensecret == "" :
        print("Please set your Access Token Secret Key")
        a = 1
    return a

def verifempty(value): # Verif Empty Value
    if value == "":
        print("Please input something, the program close now")
        exit()

def main():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    okvalue = verifvalue(consumer_key,consumer_secret,access_token,access_token_secret)
    auth = auth(consumer_key,consumer_secret,access_token,access_token_secret)
    api = createapi(auth)
    testauth(api)
    print("Please imput the URL of the image/video url list \n")
    urllink=str(input())
    verifempty(urllink)
    dlmedia(urllink,"url.txt")
    urllist = madealistfromfile()
    for i in range(len(urllist)):

