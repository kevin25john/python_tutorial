from django import forms
from sign_up.models import signupModel
class SignupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = ['first_name','last_name','email_address',
                  'tech256_username','webste_url','newsletter_preference','talk_description','active']