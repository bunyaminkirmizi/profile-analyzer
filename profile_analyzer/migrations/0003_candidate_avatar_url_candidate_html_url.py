# Generated by Django 4.1.1 on 2022-09-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_analyzer', '0002_alter_candidate_bio_alter_candidate_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='html_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]