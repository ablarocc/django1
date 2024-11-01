from django.db import models

class vestido(models.Model):
    color = models.CharField(max_length=25)
    escote = models.CharField(max_length=20)
    mangas = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.color} {self.escote} {self.mangas} '
    
