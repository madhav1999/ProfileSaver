from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.


# class User(models.Model):
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=50)

choiceoptions = [("Male", "Male"), ("Female", "Female")]


class details(models.Model):
    # field that accepts url type in database
    FirstName = models.CharField(
        max_length=50, unique=False, null=True, default=None)
    LastName = models.CharField(
        max_length=50, unique=False, null=True, default=None)
    Password = models.CharField(max_length=20, null=True, default=None)
    Occupation = models.CharField(max_length=40, null=True, default=None)
    gender = models.CharField(
        max_length=6, choices=choiceoptions, null=True, default=None)
    DateofBirth = models.DateField(null=True, default=None)
    State = models.CharField(max_length=40, null=True, default=None)
    Country = models.CharField(max_length=40, null=True, default=None)
    Education = models.CharField(max_length=40, null=True, default=None)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="fory")
    EmailName = models.EmailField(default='hai@123.com', null=True)

    def __str__(self):
        return self.FirstName
