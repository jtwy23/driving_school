from django.db import models

# Create your models here.


# Admin add an instructor
class instructor_information(models.Model):

    class Meta:
        verbose_name_plural = 'Instructor Information'

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name
