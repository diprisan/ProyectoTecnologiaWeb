from django import forms

'''class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()'''

class LoginForm(forms.Form): 
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget = forms.PasswordInput)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)