# Generated by Django 4.0.6 on 2022-07-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
