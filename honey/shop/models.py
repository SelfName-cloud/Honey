from django.db import models
import datetime


class Order(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    social_web = models.URLField(max_length=100)
    mail = models.EmailField(max_length=40)
    number_phone = models.PositiveBigIntegerField()
    sort_honey = models.CharField(max_length=20)
    count_honey = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

