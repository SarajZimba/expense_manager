from django.db import models
from root.utils import BaseModel
from user.models import Customer

class Expense(BaseModel):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
