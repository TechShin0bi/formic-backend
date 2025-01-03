from django.db import models
from django.conf import settings
from common.models import BaseModel

class PlanCategory(models.TextChoices):
    CATEGORY_1 = '1', 'Category 1'
    CATEGORY_2 = '2', 'Category 2'

class Plan(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    category = models.CharField(
        max_length=1,
        choices=PlanCategory.choices,
        default=PlanCategory.CATEGORY_1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name}'s {self.plan.name}"
    
    

    def calculate_referral_bonus(self):
        # Calculate 20% of the user's daily revenue as a referral bonus
        bonus = self.plan.daily_revenue * 0.2
        referrer = self.user.referred_by

        if referrer:
            referrer.balance += bonus  # Assuming `balance` is a DecimalField in User
            referrer.save()