# Generated by Django 3.0.1 on 2019-12-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WW_app', '0006_forum_q'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_q',
            name='timediff',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]