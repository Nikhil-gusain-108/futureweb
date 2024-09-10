from django.forms import ModelForm
from .views import Blog
class Blogform(ModelForm):
    class Meta:
        model=Blog
        fields= ("Title","Discription","img","Text","Must_read","Read_time","Type")
    
