from django import forms
sys.path.append('/ebay/cassinfra/lib')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

sys.path.append('/ebay/cassinfra/lib')