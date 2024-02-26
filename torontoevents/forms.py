from django import forms
from django.core.exceptions import ValidationError
from .models import RegisteredProgram

class RegisteredProgramForm(forms.ModelForm):
    class Meta:
        # http://127.0.0.1:8000/toronto/registeredprograms/new/
        model = RegisteredProgram
        fields = ('course_id', 'location_id', 'activity_title', 'course_title')

        #This lets us restrict form fields to specific types and add styling in attrs
        widgets = {
            'course_id': forms.NumberInput(attrs={'class': 'form-control my-5'}),
            'location_id': forms.NumberInput(attrs={'class': 'form-control my-5'}),
            'activity_title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'course_title': forms.TextInput(attrs={'class': 'form-control my-5'})
        }

        #This will change the labeling on the form fields
        labels = {
            'course_id': "Enter the course ID",
            'location_id': "Enter the location ID",
            'activity_title': "Enter the activity title",
            'course_title': "Enter the course title",
        }
    
    # This adds validation on the activity_title field to make sure it includes a key word.
    # if it doesn't, it'll return an error, otherwise it'll return the activity_title
    # In style.css we turned off default validations from django. In torontoevents/registeredprogram_form.html we are displaying it as an alert and can change the styling.
    def clean_activity_title(self):
        activity_title = self.cleaned_data['activity_title']
        # if 'Django' not in activity_title:
        #     raise ValidationError('We only accept activity titles with the word Django in it')
        return activity_title