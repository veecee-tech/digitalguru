from django.db import models

# Create your models here.


class Service(models.Model):
    service_img = models.ImageField(upload_to="images/")
    service_name = models.CharField(max_length=100)
    service_desc = models.CharField(max_length=250)

    def __str__(self):
        return self.service_name
    
