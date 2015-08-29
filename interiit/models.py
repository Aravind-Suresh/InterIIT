from django.db import models
from django.contrib.auth.models import User

FOOD_PREFERENCES = (
	('veg', 'Vegetarian') , 
	('nonveg', 'Non Vegetarian')
)

TSHIRT_TYPES = (
	('s', 'S'), 
	('m', 'M'), 
	('l', 'L'), 
	('xl', 'XL'), 
	('xxl', 'XXL')
)

SPORTS_TYPES = (
	('athletics', 'Athletics'),
	('badminton', 'Badminton'),
	('basketball', 'BasketBall'),
	('cricket', 'Cricket'),
	('football', 'Football'),
	('hockey', 'Hockey'),
	('squash', 'Squash'),
	('swimming', 'Swimming'),
	('tabletennis', 'TableTennis'),
	('tennis', 'Tennis'),
	('volleyball', 'VolleyBall'),
	('waterpolo', 'WaterPolo'),
	('weightlifting', 'Weightlifting')
)

GENDER_PREFERENCES = (
	('M', 'Male'),
	('F', 'Female')
)

class Details(models.Model):
	sport = models.CharField(max_length = 25, null = True, blank = True, choices = SPORTS_TYPES)
	user = models.ForeignKey(User)
	college =  models.CharField(max_length = 25, null = True, blank = True)

	def __unicode__(self):
		return sport + college

class Profile(models.Model):
	first_name = models.CharField(max_length = 25)
	middle_name = models.CharField(max_length = 25, null = True, blank = True)
	last_name = models.CharField(max_length = 25)

	gender = models.CharField(max_length = 1, choices = GENDER_PREFERENCES)
	date_of_birth = models.DateTimeField()

	phone_number = models.CharField(max_length = 10)
	parents_phone_number = models.CharField(max_length = 10)
	email_id = models.EmailField(max_length = 100)
	image = models.ImageField(blank = True, null = True, upload_to = 'images')

	food_preference = models.CharField(max_length = 20, choices = FOOD_PREFERENCES)
	
	tshirt_size = models.CharField(max_length = 5, choices = TSHIRT_TYPES)
	
	timestamp = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.first_name + " " + self.last_name + " " + self.middle_name
