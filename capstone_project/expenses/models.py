from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    title = models.CharField(max_length=255)          # text
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # decimal number
    category = models.CharField(max_length=100)        # text
    date = models.DateField()                          # date
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # relationship
    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamp

    def __str__(self):
        return self.title