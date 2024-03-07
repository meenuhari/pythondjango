from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=20)
    year=models.IntegerField()

    img=models.ImageField(upload_to="gallery",null=True,blank=True)
    def __str__(self):
        return self.name