from django.db import models


# Subscription Choices
class SubscriptionChoice(models.TextChoices):
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"
    PRO = "pro"


# Create your models here.
class Subscription(models.Model):
    name = models.CharField(
        max_length=30,
        choices=SubscriptionChoice.choices,
        default=SubscriptionChoice.BASIC
    )
    days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        db_table = "subscription"


# Membership Model
class Membership(models.Model):
    librarian = models.ForeignKey(
        'librarian.Librarian',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE
    )

    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subscription)

    class Meta:
        db_table = "membership"