# Generated by Django 4.2.2 on 2023-07-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_remove_listing_photo_1_remove_listing_photo_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='home_type',
            field=models.CharField(choices=[('House', 'House'), ('Apartments', 'Apartments'), ('Townhouse', 'Townhouse'), ('Vacant Land', 'Vacant Land')], default='House', max_length=50),
        ),
    ]