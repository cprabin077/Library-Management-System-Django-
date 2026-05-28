from django.db import models

# Create your models here.
from django.db import models

class GenderChoice(models.TextChoices):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

class QualificationChoice(models.TextChoices):
    SEE_SLC = "SEE/SLC", "SEE/SLC"
    INTERMEDIATE = "+2", "+2"
    BACHELOR = "Bachelors", "Bachelors"
    MASTER = "Masters", "Masters"


class Librarian(models.Model):
    full_name = models.CharField(
        max_length=200,
        help_text="Enter full name",
        verbose_name="Full Name"
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GenderChoice.choices
    )

    address = models.CharField(max_length=200)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    qualification = models.CharField(
        max_length=20,
        choices=QualificationChoice.choices
    )

    is_active = models.BooleanField(default=True)

    joining_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "librarian"

    def __str__(self):
        return self.full_name