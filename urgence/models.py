from django.db import models

# Create your models here.
class Urgence(models.Model):
    lantitude= models.DecimalField(max_length=10,max_digits=9, decimal_places=7)
    longitude=models.DecimalField(max_length=10,max_digits=9, decimal_places=7)
    descreption=models.TextField(null=True, blank=True)
    image=models.ImageField(verbose_name='description')

def image(self):
    if self.image:
        return u'<img src="%s" width="50" height="50" />' % self.image.url
    else:
        return '(Sin imagen)'
image.short_description = 'image'
image.allow_tags = True
