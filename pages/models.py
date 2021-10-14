from django.db import models


class MyPage(models.Model):
     title = models.CharField(max_length=200)
     subtitle = models.CharField(max_length=200)
     email = models.EmailField(max_length=200)
     phone = models.CharField(max_length=200)
     github = models.URLField(max_length=200, blank=True)
