from django.contrib import admin
from .models import Alumni, Student
from django.utils.html import format_html

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'year_of_graduation', 'current_job_title', 'willing_to_mentor')
    search_fields = ('full_name', 'email', 'current_company')
    list_filter = ('year_of_graduation', 'industry', 'willing_to_mentor')
    readonly_fields = ('profile_picture_tag',)

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-height: 100px;" />'.format(obj.profile_picture.url))
        return "No Image"
    profile_picture_tag.short_description = 'Profile Picture'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'current_year', 'course', 'interested_in_internships')
    search_fields = ('full_name', 'email', 'course')
    list_filter = ('current_year', 'interested_in_internships')
    readonly_fields = ('profile_picture_tag',)

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-height: 100px;" />'.format(obj.profile_picture.url))
        return "No Image"
    profile_picture_tag.short_description = 'Profile Picture'
