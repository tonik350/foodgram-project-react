# Generated by Django 3.2.15 on 2022-11-05 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipeingredient_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, help_text='Минимальное значение: 1', validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение: 1')], verbose_name='Количество'),
            preserve_default=False,
        ),
    ]
