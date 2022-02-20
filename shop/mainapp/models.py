from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return (self.name)
    


class Products(models.Model):
    name = models.CharField('Наименование', max_length=100)
    desc = models.TextField('Описание', max_length=500)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=7)
    image = models.ImageField(verbose_name='Изображение', upload_to='products', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return (self.name)

