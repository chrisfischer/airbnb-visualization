# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('count', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('listing_url', models.URLField()),
                ('scrape_id', models.IntegerField()),
                ('last_scraped', models.DateField()),
                ('name', models.CharField(max_length=400)),
                ('summary', models.CharField(max_length=400)),
                ('space', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=400)),
                ('experiences_offered', models.CharField(max_length=400)),
                ('neighborhood_overview', models.CharField(max_length=400)),
                ('notes', models.CharField(max_length=400)),
                ('transit', models.CharField(max_length=400)),
                ('access', models.CharField(max_length=400)),
                ('interaction', models.CharField(max_length=400)),
                ('house_rules', models.CharField(max_length=400)),
                ('thumbnail_url', models.URLField()),
                ('medium_url', models.URLField()),
                ('picture_url', models.URLField()),
                ('xl_picture_url', models.URLField()),
                ('host_id', models.IntegerField()),
                ('host_url', models.URLField()),
                ('host_name', models.CharField(max_length=30)),
                ('host_since', models.DateField()),
                ('host_location', models.CharField(max_length=400)),
                ('host_about', models.CharField(max_length=400)),
                ('host_response_time', models.CharField(max_length=40)),
                ('host_response_rate', models.IntegerField()),
                ('host_is_superhost', models.BooleanField()),
                ('host_thumbnail_url', models.URLField()),
                ('host_picture_url', models.URLField()),
                ('host_neighbourhood', models.CharField(max_length=40)),
                ('host_listings_count', models.IntegerField()),
                ('host_total_listings_count', models.IntegerField()),
                ('host_verifications', models.CharField(max_length=100)),
                ('host_has_profile_pic', models.BooleanField()),
                ('host_identity_verified', models.BooleanField()),
                ('street', models.CharField(max_length=100)),
                ('neighbourhood', models.CharField(max_length=40)),
                ('neighbourhood_cleansed', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('market', models.CharField(max_length=20)),
                ('smart_location', models.CharField(max_length=30)),
                ('country_code', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=15)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_location_exact', models.BooleanField()),
                ('property_type', models.CharField(max_length=20)),
                ('room_type', models.CharField(max_length=20)),
                ('accommodates', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('bed_type', models.CharField(max_length=20)),
                ('amenities', models.CharField(max_length=400)),
                ('square_feet', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weekly_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('monthly_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('security_deposit', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cleaning_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('guests_included', models.IntegerField()),
                ('extra_people', models.DecimalField(decimal_places=2, max_digits=5)),
                ('minimum_nights', models.IntegerField()),
                ('maximum_nights', models.IntegerField()),
                ('calendar_updated', models.CharField(max_length=20)),
                ('availability_30', models.IntegerField()),
                ('availability_60', models.IntegerField()),
                ('availability_90', models.IntegerField()),
                ('availability_365', models.IntegerField()),
                ('calendar_last_scraped', models.DateField()),
                ('number_of_reviews', models.IntegerField()),
                ('first_review', models.DateField()),
                ('last_review', models.DateField()),
                ('review_scores_rating', models.IntegerField()),
                ('review_scores_accuracy', models.IntegerField()),
                ('review_scores_cleanliness', models.IntegerField()),
                ('review_scores_checkin', models.IntegerField()),
                ('review_scores_communication', models.IntegerField()),
                ('review_scores_location', models.IntegerField()),
                ('review_scores_value', models.IntegerField()),
                ('requires_license', models.BooleanField()),
                ('instant_bookable', models.BooleanField()),
                ('cancellation_policy', models.CharField(max_length=20)),
                ('require_guest_profile_picture', models.BooleanField()),
                ('require_guest_phone_verification', models.BooleanField()),
                ('calculated_host_listings_count', models.IntegerField()),
                ('reviews_per_month', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
