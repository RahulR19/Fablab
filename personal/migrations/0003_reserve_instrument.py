# Generated by Django 2.0.5 on 2018-05-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20180531_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='Instrument',
            field=models.CharField(default='No Instrument Selected', max_length=30),
        ),
    ]
