from django import forms
from django.forms import ModelForm
from hospital.models import Patient

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Patient
        fields = ['first_name','last_name','username','gender','city','code','patient','phone_no','birthday']

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        if Patient.objects.filter(username__iexact=uname).exists():
            raise forms.ValidationError('Username is not valid,try again!')
        return uname

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
