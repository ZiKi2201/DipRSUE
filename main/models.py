from django.db import models
from django.core.validators import EmailValidator

class Reviews(models.Model):
    name_org = models.CharField('Организация', max_length=100)
    position = models.CharField('Должность', max_length=50)
    name = models.CharField('Имя автора', max_length=50)
    review = models.TextField('Отзыв')
    date = models.DateField('Дата написания', auto_now=True)
    consent = models.BooleanField('Согласие на обработку персональных данных', default=False)
    publication = models.BooleanField('Публикация', default=False)

    def __str__(self):
        return self.name_org

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Applications(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта', max_length=100, blank='True')
    mobile = models.CharField('Номер телефона', max_length=50, help_text='Укажите в формате: +7 000 000-00-00')
    add_inf = models.TextField('Дополнительная информация', blank='True')
    consent = models.BooleanField('Согласие на обработку персональных данных', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'