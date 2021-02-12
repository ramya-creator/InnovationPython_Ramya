from django import forms
from .models import UserDetails

class NameForm(forms.ModelForm):
    #Username = forms.CharField(label='Username', max_length=20)
    class Meta:
        model = UserDetails
        fields = "__all__"
