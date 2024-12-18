# Generated by Django 5.1.2 on 2024-10-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/alumni/'),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/students/'),
        ),
    ]
