# Generated by Django 3.1.3 on 2020-11-04 05:38

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Realtor', models.CharField(max_length=150)),
                ('Image1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Image2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Image3', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Image4', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Bedrooms', models.IntegerField()),
                ('Bathrooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.IntegerField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquirer', to='estateapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bidamount', models.IntegerField()),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='estateapp.listing')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='estateapp.profile')),
            ],
        ),
    ]
