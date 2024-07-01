from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Leadership(models.Model):
    fullname = models.CharField(verbose_name= "F.I.O", max_length=250)
    image = models.ImageField(verbose_name= "Rasm", null=True, blank=True)
    career= models.CharField(verbose_name= "Lavozimi", max_length=250)
    reception_time = models.CharField(verbose_name= "Qabul vaqti", max_length=250)
    phone = models.CharField(verbose_name= "Telefon raqami", max_length=250)
    activity = RichTextField(verbose_name="Mehnat faoliyati", null=True, blank=True)
    commitment = RichTextField(verbose_name="Funksiyanal majburiyati", null=True, blank=True)

    def __str__(self):
        return self.fullname
        

