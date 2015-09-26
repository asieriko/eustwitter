from django.shortcuts import render
from django.http import HttpResponse, redirect

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
    langsd = defaultdict(int)
    for tweet in user_timeline:       
        l = tweet['lang'] if tweet['lang'] in langs else "eu"
        langsd[l] += 1
        if l == 'eu': eus += 1
        string += l + "(" + tweet['lang'] + ")" + ": " + tweet['text'] + "<br>"
        maxids[account] = tweet['id']
    per = eus*100/len(user_timeline)
    for key in langsd.keys():
        langsd[key] = langsd[key]*100/sum(langsd.values())
    return HttpResponse("Results for account: " + account + " <br>" + "Euskara percentage: " + str(per) + "%<br>" + ', '.join(['{}% = {}'.format(k,v) for k,v in langsd.items()]) + "<br>Last tweets: <br>" + string)

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/' + form.cleaned_datatwitter_name])
            return redirect('index', account=form.cleaned_data[twitter_name])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
