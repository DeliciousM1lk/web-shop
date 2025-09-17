from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Описание", blank=True)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
