from django.db import models

# Create your models here.
class Category(models.Model):
    username = models.CharField(max_length=200,unique=True)
    
    def __unicode__(self):
        return self.username