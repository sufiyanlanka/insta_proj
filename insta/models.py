from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
	followers=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
	following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
class userpost(models.Model):
	username=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
	profilepic=models.ImageField(upload_to = 'profilepic',blank=True,null=True,default="face.jpg")
	def __str__(self):
		return self.username.username
class postuploads(models.Model):
	username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_name")
	postpic=models.ImageField(upload_to = 'postpic',blank=True)
	posttime= models.DateTimeField(auto_now_add=True)
	likes=models.ManyToManyField(User,blank=True,related_name="likes")
	comments=models.TextField(blank=True,null=True)
	def __str__(self):
		return self.username.username