from django.db import models

# Create your models here.
class Alumni(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100)

    # Professional Information
    current_job_title = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    career_path = models.TextField(blank=True)
    achievements = models.TextField(blank=True)

    # Engagement and Interests
    willing_to_mentor = models.BooleanField(default=False)
    mentorship_expertise = models.TextField(blank=True)  # List of skills/areas for mentoring
    preferred_interaction_mode = models.CharField(max_length=50, choices=[('email', 'Email'), ('video_call', 'Video Call'), ('in_person', 'In Person')])
    time_commitment = models.IntegerField(help_text="Available hours per month", blank=True, null=True)
    interested_in_career_talks = models.BooleanField(default=False)
    access_to_opportunities = models.BooleanField(default=False)  # Internship/Job Opportunities

    # Additional Contributions
    willing_to_donate = models.BooleanField(default=False)
    event_participation = models.BooleanField(default=False)
    other_contributions = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
    
class Student(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    current_year = models.IntegerField()
    course = models.CharField(max_length=100)
    career_interests = models.TextField(blank=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField()

    # Mentorship Goals
    mentorship_goals = models.TextField(blank=True)  # Skills/areas where guidance is needed
    preferred_industry = models.CharField(max_length=100, blank=True)
    preferred_company = models.CharField(max_length=100, blank=True)
    time_availability = models.IntegerField(help_text="Available hours for mentorship", blank=True, null=True)

    # Networking and Growth
    interested_in_internships = models.BooleanField(default=False)
    willing_to_attend_events = models.BooleanField(default=False)
    specific_alumni_to_connect = models.TextField(blank=True)  # Optional

    # Future Contributions
    open_to_mentoring_juniors = models.BooleanField(default=False)
    networking_groups = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
