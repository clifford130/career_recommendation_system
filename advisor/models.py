# from django.db import models

# # Create your models here.
from django.db import models

# Placeholder for future use.
class UserProfile(models.Model):
    skills = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    interests = models.CharField(max_length=255)

    def __str__(self):
        return f'Profile: {self.education}'
