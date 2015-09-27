from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm

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

def results(request,account,num=10):
    user_timeline=twitter.get_user_timeline(screen_name=account, count=num)
    eus = 0
    string=''
    langsd = defaultdict(int)
    for tweet in user_timeline:       
        l = tweet['lang'] if tweet['lang'] in langs else "eu"
        tweet['lang2'] = l
        langsd[l] += 1
        maxids[account] = tweet['id']
    tot = sum(langsd.values())
    for key in langsd.keys():
        langsd[key] = langsd[key]*100/tot
    form = NameForm()
    return render(request, 'results.html', {'name': account, 'langs': dict(langsd), 'tweets': user_timeline,'form':form})


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
            #return HttpResponseRedirect('/' + form.cleaned_data['twitter_name'])
            num = 10
            account = form.cleaned_data['twitter_name']
            user_timeline=twitter.get_user_timeline(screen_name=account, count=num)
            langsd = defaultdict(int)
            for tweet in user_timeline:
                l = tweet['lang'] if tweet['lang'] in langs else "eu"
                tweet['lang2'] = l
                langsd[l] += 1
                maxids[account] = tweet['id']
            tot = sum(langsd.values())
            for key in langsd.keys():
                langsd[key] = langsd[key]*100/tot
            form = NameForm()
            return render(request, 'results.html', {'name': account, 'langs': dict(langsd), 'tweets': user_timeline,'form':form})
            #return redirect('results', account=form.cleaned_data['twitter_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
