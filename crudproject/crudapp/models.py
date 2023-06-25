from django.db import models

# Create your models here.
class Project(models.Model):
    Name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    project=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

