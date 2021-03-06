# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Listing model for the database
class Listing(models.Model):
	id = models.IntegerField(primary_key=True)
	listing_url = models.CharField(max_length=300)
	scrape_id = models.DecimalField(max_digits=20, decimal_places=0)
	last_scraped = models.DateField()
	name = models.CharField(max_length=400)
	summary = models.CharField(max_length=10000)
	space = models.CharField(max_length=10000)
	description = models.CharField(max_length=10000)
	experiences_offered = models.CharField(max_length=10000)
	neighborhood_overview = models.CharField(max_length=10000)
	notes = models.CharField(max_length=10000)
	transit = models.CharField(max_length=10000)
	access = models.CharField(max_length=10000)
	interaction = models.CharField(max_length=10000)
	house_rules = models.CharField(max_length=10000)
	thumbnail_url = models.CharField(max_length=300)
	medium_url = models.CharField(max_length=300)
	picture_url = models.CharField(max_length=300)
	xl_picture_url = models.CharField(max_length=300)
	host_id = models.IntegerField()
	host_url = models.CharField(max_length=300)
	host_name = models.CharField(max_length=300)
	host_since = models.DateField()
	host_location = models.CharField(max_length=400)
	host_about = models.CharField(max_length=50000)
	host_response_time = models.CharField(max_length=40)
	host_response_rate = models.CharField(max_length=5)
	host_acceptance_rate = models.CharField(max_length=3)
	host_is_superhost = models.BooleanField()
	host_thumbnail_url = models.CharField(max_length=300)
	host_picture_url = models.CharField(max_length=300)
	host_neighbourhood = models.CharField(max_length=2000)
	host_listings_count = models.IntegerField()
	host_total_listings_count = models.IntegerField()
	host_verifications = models.CharField(max_length=1000)
	host_has_profile_pic = models.BooleanField()
	host_identity_verified = models.BooleanField()
	street = models.CharField(max_length=2000)
	neighbourhood = models.CharField(max_length=2000)
	neighbourhood_cleansed = models.CharField(max_length=2000)
	neighbourhood_group_cleansed = models.CharField(max_length=1)
	city = models.CharField(max_length=400)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	market = models.CharField(max_length=40)
	smart_location = models.CharField(max_length=40)
	country_code = models.CharField(max_length=2)
	country = models.CharField(max_length=15)
	latitude = models.DecimalField(max_digits=15, decimal_places=8)
	longitude = models.DecimalField(max_digits=15, decimal_places=8)
	is_location_exact = models.BooleanField()
	property_type = models.CharField(max_length=20)
	room_type = models.CharField(max_length=20)
	accommodates = models.IntegerField()
	bathrooms = models.DecimalField(max_digits=5, decimal_places=1)
	bedrooms = models.IntegerField()
	beds = models.IntegerField()
	bed_type = models.CharField(max_length=20)
	amenities = models.CharField(max_length=4000)
	square_feet = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	weekly_price = models.DecimalField(max_digits=10, decimal_places=2)
	monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
	security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
	cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
	guests_included = models.IntegerField()
	extra_people = models.DecimalField(max_digits=10, decimal_places=2)
	minimum_nights = models.IntegerField()
	maximum_nights = models.IntegerField()
	calendar_updated = models.CharField(max_length=20)
	has_availability = models.BooleanField()
	availability_30 = models.IntegerField()
	availability_60 = models.IntegerField()
	availability_90 = models.IntegerField()
	availability_365 = models.IntegerField()
	calendar_last_scraped = models.DateField()
	number_of_reviews = models.IntegerField()
	first_review = models.DateField()
	last_review = models.DateField()
	review_scores_rating = models.IntegerField()
	review_scores_accuracy = models.IntegerField()
	review_scores_cleanliness = models.IntegerField()
	review_scores_checkin = models.IntegerField()
	review_scores_communication = models.IntegerField()
	review_scores_location = models.IntegerField()
	review_scores_value = models.IntegerField()
	requires_license = models.BooleanField()
	license = models.CharField(max_length=1000)
	jurisdiction_names = models.CharField(max_length=60)
	instant_bookable = models.BooleanField()
	cancellation_policy = models.CharField(max_length=20)
	require_guest_profile_picture = models.BooleanField()
	require_guest_phone_verification = models.BooleanField()
	calculated_host_listings_count = models.IntegerField()
	reviews_per_month = models.DecimalField(max_digits=5, decimal_places=2)

	# helper function that returns just the numerical fields and their respective 'pretty' names
	def get_numerical_fields():
		return {
			'Len. Summary': 'length(summary)',
			'Len. Space Desc.': 'length(space)',
			'Len. Description': 'length(description)',
			'Len. House Rules': 'length(house_rules)',
			'Host: Len. About': 'length(host_about)',
			'Host: Superhost': 'host_is_superhost',
			'Host: Num. Listings': 'host_total_listings_count',
			'Accommodates': 'accommodates',
			'Num. Bathrooms': 'bathrooms',
			'Num. Bedrooms': 'bedrooms',
			'Square Feet': 'square_feet',
			'Price': 'price',
			'Weekly Price': 'weekly_price',
			'Monthly Price': 'monthly_price',
			'Security Deposit': 'security_deposit',
			'Cleaning Fee': 'cleaning_fee',
			'Min nights': 'minimum_nights',
			'Max nights': 'maximum_nights',
			'Num. Reviews': 'number_of_reviews',
			'Reviews: Rating': 'review_scores_rating',
			'Reviews: Accuracy': 'review_scores_accuracy',
			'Reviews: Cleanliness': 'review_scores_cleanliness',
			'Reviews: Checkin': 'review_scores_checkin',
			'Reviews: Commun.': 'review_scores_communication',
			'Reviews: Location': 'review_scores_location',
			'Reviews: Value': 'review_scores_value'
		}
