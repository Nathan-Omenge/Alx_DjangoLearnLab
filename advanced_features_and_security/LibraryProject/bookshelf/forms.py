from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label="Title contains", max_length=100, required=False)

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)