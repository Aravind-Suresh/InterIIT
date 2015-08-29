from django.forms import ModelForm
from interiit.models import Profile

class ProfileRegistrationForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['timestamp', 'user']