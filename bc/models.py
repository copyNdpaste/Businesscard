from django.db import models

# Create your models here.
class Businesscard(models.Model):
    company_name = models.CharField(max_length=30)
    position = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    company_addr = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    site_addr = models.CharField(max_length=50)

    def __str__(self):
        return str(self.company_name) + ' ' + str(self.name)