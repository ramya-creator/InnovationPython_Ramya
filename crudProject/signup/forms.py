from django import forms
from .models import SignupDetails

class NameForm(forms.ModelForm):
    class Meta:
        model = SignupDetails
        fields = "__all__"
