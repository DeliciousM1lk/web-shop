from django.db import models


# Create your models here.
def product_image_path(instance, filename):
    return f"products/{instance.product_id}/{filename}"


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Слаг", max_length=200, unique=True, null=True, blank=True)
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

    @property
    def main_image(self):
        return self.images.filter(is_main=True).first() or self.images.first()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to=product_image_path)
    is_main = models.BooleanField(verbose_name='Главное изображение', default=False)
    alt = models.CharField(verbose_name='Альтернативный текст', max_length=200, blank=True)
    created_at = models.DateTimeField(verbose_name='Загружено', auto_now_add=True)

    class Meta:
        ordering = ['product']
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"

    def __str__(self):
        return f'{self.pk} - {self.product.name}'
