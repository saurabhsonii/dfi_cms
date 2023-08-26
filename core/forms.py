from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone_number', 'message']

    # phone_number = forms.IntegerField()

# class CustomUser(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'name','phone_number', 'address','profile_image']