from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.TextField(null = 'TRUE', blank = 'True', max_length = 2000)

class Tag(models.Model):
    name = models.TextField(null = 'TRUE', blank = 'True', max_length = 2000)

class Good(models.Model):
           
    file = models.FileField(null = 'TRUE', blank = 'True',  upload_to='goods/')
    name = models.TextField(null = 'TRUE', blank = 'True', max_length = 2000)
    shop = models.ForeignKey(Shop, null = 'TRUE', blank = 'True', on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag, blank='True')
    created_at = models.DateTimeField(auto_now_add=True)



