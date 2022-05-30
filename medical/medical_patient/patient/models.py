from django.db import models

class Patient(models.Model):
    last_name = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=50, db_index=True)
    second_name = models.CharField(max_length=50, db_index=True)
    age = models.SmallIntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    diagnosis = models.TextField(blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_agree = models.BooleanField(default=False)



    def __str__(self):
        return '{}'.format(self.last_name)
