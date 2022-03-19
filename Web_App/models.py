from django.db import models

# Create your models here.
class ContactUS(models.Model):
    name  = models.CharField(max_length=100, null=True)
    gender  = models.CharField(max_length=100, null=True)
    category  = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.IntegerField()
    subject  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name