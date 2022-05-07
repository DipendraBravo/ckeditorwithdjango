from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(null=True, blank=True)

