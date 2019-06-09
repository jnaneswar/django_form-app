from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='images',blank=False)
    stream = models.CharField(max_length=50,choices=(
                  ('cse','Cse'),('ece','Ece')

    ))
    date_added = models.DateField(auto_now_add=True)
    video = models.FileField(upload_to='videos',blank=False)

    def __str__(self):
        return self.name
    
    

