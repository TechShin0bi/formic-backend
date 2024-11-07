# Generated by Django 4.2.16 on 2024-11-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_balance_alter_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]