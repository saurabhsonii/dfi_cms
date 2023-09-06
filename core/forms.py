from django import forms
from core.models import (Contact, CustomUser, VehicleDetails, PersonalDetails,
                         OccupationDetails, DocumentImages, VehicleDocuments, Disbursement)
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone_number', 'message']


class AgentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone_number', 'address', 'profile_image']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AgentUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_number',
                  'address', 'profile_image', 'active']

    def save(self, commit=True):
        agent = super().save(commit=False)
        if commit:
            agent.save()
        return agent


# =========================================================================

class VehicleDetailsForm(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = "__all__"
        exclude = ['vehicle_type', 'created_at', 'updated_at', 'parent_id']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.required = False


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = "__all__"
        exclude = ['created_at', 'updated_at', 'vehicle_id']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.required = False


class DocumentImagesForm(forms.ModelForm):
    class Meta:
        model = DocumentImages
        fields = ['image',]

    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class OccupationDetailsForm(forms.ModelForm):
    class Meta:
        model = OccupationDetails
        fields = ['document_image',]

        document_image = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}))


class VehicleDocumentsForm(forms.ModelForm):
    class Meta:
        model = VehicleDocuments
        fields = [
            'rc_card',
            'insurance',
            'form_29_30',
            'form_34_35',
            'bank_noc',
            'rto_noc',
            'form_28',
        ]


class DisbursementForm(forms.ModelForm):
    class Meta:
        model = Disbursement
        fields = [
            'bank_name',
            'loan_amount',
            'net_amount',
            'emi_duration',

        ]
