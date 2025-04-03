from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class FinancialData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="financial_data")
    monthly_income = models.FloatField(default=0)
    monthly_spending = models.FloatField(default=0)
    expenses = models.JSONField(default=dict)  # Example: {"Food": 0, "Transport": 0, ...}
    incomes = models.JSONField(default=dict)  # Example: {"Salary": 0, "Freelancing": 0, ...}

    def __str__(self):
        return f"{self.user.username}'s Financial Data"
