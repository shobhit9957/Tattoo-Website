from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    video1 = models.FileField(upload_to="admin", validators=[file_size], default="one-off")
    video2 = models.FileField(upload_to="admin", validators=[file_size], default="one-off")
    video3 = models.FileField(upload_to="admin", validators=[file_size], default="one-off")
    video4 = models.FileField(upload_to="admin", validators=[file_size], default="one-off")
    video5 = models.FileField(upload_to="admin", validators=[file_size], default="one-off")

class Image(models.Model):
    image1 = models.ImageField(upload_to='img/%y', default='one-off')
    image2 = models.ImageField(upload_to='img/%y', default='one-off')
    image3 = models.ImageField(upload_to='img/%y', default='one-off')
    image4 = models.ImageField(upload_to='img/%y', default='one-off')
    image5 = models.ImageField(upload_to='img/%y', default='one-off')
    image6 = models.ImageField(upload_to='img/%y', default='one-off')
    image7 = models.ImageField(upload_to='img/%y', default='one-off')
    image8 = models.ImageField(upload_to='img/%y', default='one-off')
    image9 = models.ImageField(upload_to='img/%y', default='one-off')
    image10 = models.ImageField(upload_to='img/%y', default='one-off')
    image11 = models.ImageField(upload_to='img/%y', default='one-off')