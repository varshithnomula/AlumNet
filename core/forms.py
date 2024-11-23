# forms.py
from django import forms
from .models import Alumni, Student ,MentorshipRequest

class AlumniFormStep1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = Alumni
        fields = ['full_name', 'email', 'password']

class AlumniFormStep2(forms.ModelForm):
    class Meta:
        model = Alumni
        exclude = ['full_name', 'email', 'password']  # Exclude fields already covered in step 1

class StudentFormStep1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = Student
        fields = ['full_name', 'email', 'password']

class StudentFormStep2(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['full_name', 'email', 'password']  # Exclude fields already covered in step 1
class AlumniProfileForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = [
            'full_name', 'email', 'linkedin', 'location', 'profile_picture', 
            'current_job_title', 'current_company', 'career_path', 'achievements',
            'willing_to_mentor', 'mentorship_expertise', 'preferred_interaction_mode',
            'time_commitment', 'interested_in_career_talks', 'access_to_opportunities',
            'willing_to_donate', 'event_participation', 'other_contributions'
        ]

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name', 'email', 'linkedin', 'profile_picture', 'mentorship_goals',
            'career_interests', 'preferred_industry', 'preferred_company',
            'interested_in_internships', 'time_availability', 'specific_alumni_to_connect',
            'willing_to_attend_events', 'open_to_mentoring_juniors', 'networking_groups'
        ]

class MentorshipRequestForm(forms.ModelForm):
    class Meta:
        model = MentorshipRequest
        fields = ['alumni', 'request_message']