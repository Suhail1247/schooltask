from django.db import models
from django.core.validators import RegexValidator



class school(models.Model):
    name=models.CharField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('m', 'm'),
        ('f', 'f'),
    )
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    mail = models.EmailField()
    dept = models.CharField(max_length=20)
    course = models.CharField(max_length=20)


    # pen = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table='new'
