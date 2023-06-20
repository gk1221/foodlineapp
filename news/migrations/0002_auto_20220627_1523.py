# Generated by Django 3.2 on 2022-06-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pttdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('href', models.TextField()),
                ('pushcount', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]