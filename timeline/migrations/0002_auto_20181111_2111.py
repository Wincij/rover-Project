# Generated by Django 2.0.2 on 2018-11-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
