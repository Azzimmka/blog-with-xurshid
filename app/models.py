from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'
        
    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='articles')
    view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Xavola'
        verbose_name_plural = 'Xavolalar'
        
        
    def __str__(self):
        return self.title