from django import forms

class NameForm(forms.Form):
    twitter_name = forms.CharField(label='Twitter name', max_length=100)
