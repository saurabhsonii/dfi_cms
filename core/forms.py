from django import forms
# from .models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

# class CustomUser(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'name','phone_number', 'address','profile_image']