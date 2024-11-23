from django.db import models
class Alumni(models.Model):
    full_name = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    linkedin = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/alumni/', blank=True, null=True)
    current_job_title = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    career_path = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    willing_to_mentor = models.BooleanField(default=False)
    mentorship_expertise = models.TextField(blank=True)
    preferred_interaction_mode = models.CharField(
        max_length=50, 
        choices=[('email', 'Email'), ('video_call', 'Video Call'), ('in_person', 'In Person')]
    )
    time_commitment = models.IntegerField(blank=True, null=True)
    interested_in_career_talks = models.BooleanField(default=False)
    access_to_opportunities = models.BooleanField(default=False)
    willing_to_donate = models.BooleanField(default=False)
    event_participation = models.BooleanField(default=False)
    other_contributions = models.TextField(blank=True)
    password = models.CharField(max_length=128,default="")

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    current_year = models.IntegerField()
    course = models.CharField(max_length=100)
    career_interests = models.TextField(blank=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/students/', blank=True, null=True)
    mentorship_goals = models.TextField(blank=True)
    preferred_industry = models.CharField(max_length=100, blank=True)
    preferred_company = models.CharField(max_length=100, blank=True)
    time_availability = models.IntegerField(blank=True, null=True)
    interested_in_internships = models.BooleanField(default=False)
    willing_to_attend_events = models.BooleanField(default=False)
    specific_alumni_to_connect = models.TextField(blank=True)
    open_to_mentoring_juniors = models.BooleanField(default=False)
    networking_groups = models.BooleanField(default=False)
    password=models.CharField(max_length=128,default="")
    def __str__(self):
        return self.full_name

class MentorshipRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='mentorship_requests')
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='received_requests')
    request_message = models.TextField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
