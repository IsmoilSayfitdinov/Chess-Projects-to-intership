# Generated by Django 5.0.7 on 2024-07-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='round_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]