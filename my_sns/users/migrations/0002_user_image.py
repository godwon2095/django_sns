# Generated by Django 2.0.13 on 2019-03-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='none/default_profile.jpg', upload_to='image/', verbose_name='Image of User'),
        ),
    ]
