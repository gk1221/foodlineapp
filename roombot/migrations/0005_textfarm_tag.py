# Generated by Django 3.2 on 2021-09-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombot', '0004_auto_20210907_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfarm',
            name='tag',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
