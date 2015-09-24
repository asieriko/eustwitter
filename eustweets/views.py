from django.shortcuts import render
from django.http import HttpResponse

from twython import Twython
from collections import defaultdict

from . import keys
 
twitter = Twython(keys.APP_KEY, keys.APP_SECRET)

auth = twitter.get_authentication_tokens(callback_url='http://iesmendillorribhi.educacion.navarra.es/blogs')

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
auth['auth_url']

langs = ['en','eu','es','fr','de']
maxids = defaultdict(str)
accounts=['iesmendibhi','infomendi']


#for account in accounts:
    #user_timeline=twitter.get_user_timeline(screen_name=account, count=10,since_id='430943667051069440')
    #print(account)
    #for tweet in user_timeline:       
        #l = tweet['lang'] if tweet['lang'] in langs else "eu"
        #print(l + "(" + tweet['lang'] + ")" + ": " + tweet['text'] + "\n") 
        #maxids[account] = tweet['id']


def index(request,account,num=10):
    user_timeline=twitter.get_user_timeline(screen_name=account, count=num)
    eus = 0
    string=''
    for tweet in user_timeline:       
        l = tweet['lang'] if tweet['lang'] in langs else "eu"
        if l == 'eu': eus += 1
        string += l + "(" + tweet['lang'] + ")" + ": " + tweet['text'] + "<br>"
        maxids[account] = tweet['id']
    per = eus*100/len(user_timeline)
    return HttpResponse("Results for account: " + account + " <br>" + "Euskara percentage: " + str(per) + "%<br>" + "Last tweets: <br>" + string)
