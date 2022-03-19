from django.db import models

# Create your models here.
class Adoption(models.Model):
    name  = models.CharField(max_length=100, null=True)
    gender  = models.CharField(max_length=100, null=True)
    category  = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.IntegerField()
    message  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
        

class Animal(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    age = models.IntegerField()
    gender  = models.CharField(max_length=100, null=True)
    category  = models.CharField(max_length=100, null=True)
    desc = models.TextField(max_length=3000, null=True)
    email = models.EmailField()
    number = models.IntegerField()
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url