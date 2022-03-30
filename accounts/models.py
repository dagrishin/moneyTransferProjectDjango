from django.contrib.auth.models import User
from django.db import models


class UserAccount(models.Model):
    user = models.OneToOneField(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )
    account_no = models.UUIDField()
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    create_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.account_no)
