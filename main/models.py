from django.db import models
from django.urls import reverse
import os.path


class Country(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    capital = models.CharField('Столица', max_length=100, unique=True)
    info = models.TextField('Информация', max_length=10000, blank=True, null=True)
    img_country = models.ImageField('Изображение страны', upload_to='country_image', blank=True, null=True)
    flag = models.ImageField('Флаг', upload_to='flag', blank=True, null=True)
    img_capital = models.ImageField('Изображение столицы', upload_to='capital_image', blank=True, null=True)
    сontinent = models.ForeignKey('Continent', verbose_name='Континент', on_delete=models.SET_NULL,
                                  null=True)
    group = models.ForeignKey('Group', verbose_name='Группа стран', on_delete=models.SET_NULL, blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name', ]

    def __str__(self):
        return self.name[:150]

    def get_absolute_url(self):
        return reverse('country', kwargs={'pk': self.pk})


class Continent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField('Изображение континента', upload_to='сontinent_image', blank=True, null=True)

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенты'

    def __str__(self):
        return self.name[:15]

    def get_absolute_url(self):
        return reverse('сontinent', kwargs={'pk': self.pk})


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Группа стран'
        verbose_name_plural = 'Группы стран'

    def __str__(self):
        return self.name[:15]

    def get_absolute_url(self):
        return reverse('group', kwargs={'pk': self.pk})
