from django.db import models


class ProductTypes(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(default='', null=False)

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Тип продуктов'

    def __str__(self):
        return (self.name)
    


class Products(models.Model):
    name = models.CharField('Наименование', max_length=100)
    desc = models.CharField('Описание', max_length=500)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=7)
    image = models.ImageField(verbose_name='Изображение', upload_to='products', blank=True)
    product_type = models.ForeignKey(ProductTypes, verbose_name='Тип продукта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return (self.name)
