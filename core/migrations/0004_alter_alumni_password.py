# Generated by Django 5.1.2 on 2024-11-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alumni_password_alter_alumni_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
