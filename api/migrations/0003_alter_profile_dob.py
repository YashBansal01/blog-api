# Generated by Django 4.0.6 on 2022-07-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_post_options_post_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]