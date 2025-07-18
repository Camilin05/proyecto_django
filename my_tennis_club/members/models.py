from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id} {self.firstname} {self.lastname}"