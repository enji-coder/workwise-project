# Generated by Django 3.0.1 on 2019-12-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WW_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='profile_pic',
            field=models.FileField(default='images/mypic.png', upload_to='WW_app/images/'),
        ),
    ]