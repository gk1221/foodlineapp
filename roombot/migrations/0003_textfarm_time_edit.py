# Generated by Django 3.2 on 2021-05-24 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roombot', '0002_alter_textfarm_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfarm',
            name='time_edit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
