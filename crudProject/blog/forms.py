from django import forms
from .models import newblog

class NameForm(forms.ModelForm):
    class Meta:
        model = newblog
        fields = "__all__"
