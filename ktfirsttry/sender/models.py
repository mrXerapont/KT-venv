from django.db import models

# Create your models here.

class Repeat_type(models.Model):
    repeat_name = models.CharField(max_length=20, verbose_name = 'Частота повторения')

    def __str__(self):
        return self.repeat_name
    
    class Meta:
        verbose_name_plural = 'Частота повторения'
        verbose_name = 'Частота повторения'
        #ordering = ['repeat_name']

class Snd(models.Model):
    #id = models.AutoField(primary_key=True)
    description = models.TextField (null=True, blank=True, verbose_name='Описание задачи')
    mailto = models.EmailField(verbose_name='E-mail получателя')
    text = models.TextField(verbose_name='Текст уведомления')
    dtime = models.DateTimeField(auto_now=False,verbose_name='Дата\время отправки')
    
    repeat = models.ForeignKey('Repeat_type', on_delete=models.PROTECT, default=1, verbose_name='Частота повторения')

    class Meta:
        verbose_name_plural = 'Информатор'
        verbose_name = 'Информатор'
        ordering = ['dtime']
    
