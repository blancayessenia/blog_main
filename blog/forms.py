from django import forms

from .models import Comment

class ComentFrom(forms.ModelForm):

    class meta:
        model = Commentfields = ['name','email','body']
        