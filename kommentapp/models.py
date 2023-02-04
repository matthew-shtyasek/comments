from django.db import models

class KommentModel(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    
    
