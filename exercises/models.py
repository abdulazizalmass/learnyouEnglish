from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class exercise(models.Model):
	user = models.ForeignKey('auth.User')
	question = models.TextField()
	answer = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def answeringDate(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.question
