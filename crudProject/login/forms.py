from django import forms
from .models import LoginDetails

class NameForm(forms.ModelForm):
    class Meta:
        model = LoginDetails
        fields = "__all__"
