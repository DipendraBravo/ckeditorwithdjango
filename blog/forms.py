from django import forms
from .models import *

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'