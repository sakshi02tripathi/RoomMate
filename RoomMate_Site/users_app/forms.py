from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserInfoForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")

    # Add the fields for roommate preferences
    age = forms.IntegerField(required=True, label="Age")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], label="Gender")
    location_preference = forms.CharField(max_length=100, required=True, label="Location Preference")
    occupation = forms.CharField(max_length=100, required=True, label="Occupation")

    # Roommate Preferences
    smoking = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Smoking")
    pets = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Pets")
    cleanliness = forms.ChoiceField(choices=[('Neat', 'Neat'), ('Messy', 'Messy')], label="Cleanliness")
    sleep_schedule = forms.ChoiceField(choices=[('Early bird', 'Early bird'), ('Night owl', 'Night owl')],
                                       label="Sleep Schedule")
    work_schedule = forms.ChoiceField(choices=[('Work from home', 'Work from home'), ('Commute', 'Commute')],
                                      label="Work Schedule")

    # Budget as a choice for simplicity; could also use a slider in the frontend
    budget = forms.IntegerField(required=True, label="Budget")

    # Interests/Hobbies as a multiple choice field
    interests_hobbies = forms.MultipleChoiceField(
        choices=[('Sports', 'Sports'), ('Music', 'Music'), ('Gaming', 'Gaming')],
        widget=forms.CheckboxSelectMultiple,
        label="Interests/Hobbies"
    )
