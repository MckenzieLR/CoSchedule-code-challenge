# Generated by Django 4.2.1 on 2023-05-31 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coschedulecodechallengeapi', '0002_alter_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
    ]
