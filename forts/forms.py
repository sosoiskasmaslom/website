from django import forms

class make_excursion_page(forms.Form):
    meet_place = forms.CharField(max_length=100)
    time = forms.DateTimeField()
    count = forms.IntegerField()

class make_fort_page(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea)