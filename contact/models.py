from django.db import models

# Create your models here.

class Con (models.Model):
    firstname=models.CharField(max_length=200)
    Subject=models.TextField()
    email=models.EmailField()
   

    def __str__(self):
        return self.firstname