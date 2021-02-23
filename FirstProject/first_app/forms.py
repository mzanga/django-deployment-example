from django import forms
from django.contrib.auth.models import User as DUser
from first_app.models import User
from first_app.models import UserProfileInfo
from django.core import validators

# Create your forms here.

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = DUser
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class FormName(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


def check_for_z(value):
    if value[0].lower() == "z":
        raise forms.ValidationError("First name cannot start with Z!")

class FormName_(forms.Form):
    first_name = forms.CharField(max_length=268, validators=[check_for_z])
    last_name = forms.CharField(max_length=268)
    email_address = forms.EmailField()
    verified_email_address = forms.EmailField(label="Enter your email again:")
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email_address']
        vemail = all_clean_data['verified_email_address']
        if email != vemail:
            raise forms.ValidationError("Make sure your email match!")
