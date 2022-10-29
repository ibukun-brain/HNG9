from django.db import models

# Create your models here.
class HNGProfile(models.Model):
    slackUsername = models.CharField("slackUsername", max_length=200)
    backend = models.BooleanField(default=True)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.slackUsername