# Generated by Django 5.0.3 on 2024-06-10 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academyUser', '0002_remove_account_id_alter_account_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]