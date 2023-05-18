from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20,min_length=2)
    surname = forms.CharField(label='Surname',max_length=50,min_length=2)
    feedback = forms.CharField(label='Feedback',max_length=50,min_length=2,widget=forms.Textarea(attrs={'rows':4,'cols':20}))
    rating = forms.IntegerField(label='Rating',min_value=1,max_value=5)

