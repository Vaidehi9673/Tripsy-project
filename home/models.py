from django.db import models

# Create your models here.
class Contact(models.Model):
    Sr=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    text=models.TextField()

    def __str__(self):
        return self.uname