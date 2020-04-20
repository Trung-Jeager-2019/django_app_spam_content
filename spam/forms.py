from django import forms
from .models import Spam_content

class SpamForm(forms.ModelForm):
    class Meta:
        model = Spam_content
        fields = ['content']
