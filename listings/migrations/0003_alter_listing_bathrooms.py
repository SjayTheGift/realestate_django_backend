# Generated by Django 4.2.2 on 2023-07-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]