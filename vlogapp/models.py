from django.db import models

# Create your models here.
class current(models.Model):
   title=models.CharField(max_length=100)
   img=models.ImageField(upload_to='vlog pictures')
   category=models.TextField()
   desc=models.TextField()
   month = models.CharField(max_length=20)
   day=models.IntegerField()
