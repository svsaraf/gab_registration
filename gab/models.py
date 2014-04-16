from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	verified = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.user.username
# Create your models here.
