from django.db import models
from django_quill.fields import QuillField

# Create your models here.
# Blog
class Blog(models.Model):
	Title = models.CharField(max_length=50)
	Discription = models.CharField(max_length=200)
	img = models.ImageField(upload_to="media")
	Text = QuillField()
	Must_read = models.BooleanField(default=False)
	Read_time = models.IntegerField()
	Type = models.CharField( choices=(("normal","normal"),("airdrop","airdrop")),max_length=50,default="normal")
	Created_date = models.DateField(auto_now=True)
	Created_time = models.TimeField(auto_now=True)
	id = models.AutoField(primary_key= True)
	def __str__(self):
		return f'{self.Title} {self.id}'
# Socials
class Socials(models.Model):
	telegram = models.URLField( max_length=300)
	You_tube = models.URLField( max_length=300)
	Instagram = models.URLField( max_length=300)
	X = models.URLField( max_length=300)

# Hot airdrops
class Hotdrops(models.Model):
	Name = models.CharField(max_length = 20)
	blog = models.OneToOneField(Blog,on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.Name} {self.id}'
# add this to notion docs
# upcoming airdrops
class upcomingairdrops(models.Model):
	Name = models.CharField(max_length=50)
	blog = models.OneToOneField(Blog,on_delete=models.CASCADE)
	discription = models.CharField( max_length=170)
	id = models.AutoField(primary_key=True)
	def __str__(self):
		return f'{self.Name} {self.id}'