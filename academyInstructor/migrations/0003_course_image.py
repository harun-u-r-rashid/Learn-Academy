# Generated by Django 5.0.3 on 2024-06-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyInstructor', '0002_alter_instructor_image_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/'),
        ),
    ]
