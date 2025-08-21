from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label="Title contains", max_length=100, required=False)