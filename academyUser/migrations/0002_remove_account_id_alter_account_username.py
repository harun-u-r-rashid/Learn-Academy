# Generated by Django 5.0.3 on 2024-06-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
