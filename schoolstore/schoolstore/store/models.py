from django.db import models

# Create your models here.
class Purchase(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phno = models.IntegerField()
    mail = models.EmailField()
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    material1 = models.CharField(max_length=250, default='0000000')
    material2 = models.CharField(max_length=250, default='0000000')
    material3 = models.CharField(max_length=250, default='0000000')
    material4 = models.CharField(max_length=250, default='0000000')
    material5 = models.CharField(max_length=250, default='0000000')
    def __str__(self):
        return self.name

