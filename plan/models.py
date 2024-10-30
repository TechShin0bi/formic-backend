from django.db import models
from django.conf import settings

class PlanCategory(models.TextChoices):
    CATEGORY_1 = '1', 'Category 1'
    CATEGORY_2 = '2', 'Category 2'

class Plan(models.Model):
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
        return f"{self.name} ({self.get_category_display()})"

class UserPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL to point to your custom User model
        on_delete=models.CASCADE,
        related_name='user_plans'
    )
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)  # Assuming a Plan model exists
    last_process = models.DateTimeField(auto_now=True)  # Track last processing date

    is_validated = models.BooleanField(default=False)  # Track validation status
    validated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Admin who validated the plan
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='validated_plans'
    )

    def __str__(self):
        return f"{self.user.name}'s {self.plan.name}"