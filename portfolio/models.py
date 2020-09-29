from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image =models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    startdate = models.DateField()
    enddate = models.DateField()
    Code = models.TextField()
    def __str__(self):
        return self.title


class Skills(models.Model):
    icon = models.ImageField(upload_to='portfolio/images')
    name = models.CharField(max_length=200)
    refer_link = models.URLField(blank=True)


    def __str__(self):
            return self.name
