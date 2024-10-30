# Generated by Django 4.2.16 on 2024-10-30 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_withdrawal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='validated_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_admin': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='validated_withdrawals', to=settings.AUTH_USER_MODEL),
        ),
    ]