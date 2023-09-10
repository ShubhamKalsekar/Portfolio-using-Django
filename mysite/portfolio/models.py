from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    website = models.TextField()
    degree = models.TextField()
    phone = models.BigIntegerField()
    email = models.TextField()
    city = models.TextField()
    freelance  = models.TextField()
    about_Img = models.ImageField(upload_to='images/')

   
class Skills(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_proficiency = models.IntegerField()
    about_desc = models.TextField()

    def __str__(self):
        return self.skill_name
    

class Testinomial(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='Testinomial_images/')
    designation = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    img = models.ImageField(upload_to='Portfolio_img/')
    name = models.CharField(max_length=30)
    desc = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name