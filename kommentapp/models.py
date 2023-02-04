from django.db import models

class KommentModel(models.Model):
    name = models.CharField(max_length=32,verbose_name='Имя пользователя')
    text = models.TextField(blank=False,verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    
    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
    def __str__(self):
        return (self.text[:20] +"...")
    
    
    
