# Generated by Django 3.1.7 on 2021-04-24 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_capinitials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpeoples',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='cpeoples',
            name='profilepic',
        ),
    ]