# Generated by Django 3.2 on 2021-11-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlinebot', '0004_alter_stockrecord_earnper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockrecord',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
