# Generated by Django 4.1.1 on 2022-09-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
