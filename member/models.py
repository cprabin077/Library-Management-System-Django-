from django.db import models
from django_countries.fields import CountryField

class GenderChoice(models.TextChoices):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50, help_text="enter first name", verbose_name='First Name')
    middle_name = models.CharField(max_length=20, null=True, blank=True, help_text="enter middle name", verbose_name='Middle Name')
    last_name = models.CharField(max_length=50, help_text="enter surname", verbose_name='Last Name')
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=5, choices=GenderChoice.choices)
    country = CountryField(blank_label="Select country")
    is_active = models.BooleanField(default=False)
    joined_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.first_name
