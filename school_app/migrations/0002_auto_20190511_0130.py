# Generated by Django 2.1.7 on 2019-05-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_info',
            name='address',
            field=models.CharField(default='name', max_length=30),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='name',
            field=models.CharField(default='name', max_length=30),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='phone_no',
            field=models.IntegerField(blank=True, default='345353'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='website',
            field=models.CharField(default='name', max_length=30),
        ),
    ]
