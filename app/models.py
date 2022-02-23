from django.db import models

# Create your models here.
class multipleSearchFields(models.Model):
    emid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    occapation = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.empname
