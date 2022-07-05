from django.db import models
from datetime import datetime
from django.contrib.auth.models import auth, User




class profile(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.CharField(max_length=40)
    Detail= models.TextField()
    image = models.ImageField(upload_to='post_image', default=None)
    date = models.DateTimeField(default= datetime.now(), blank=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.Text


class Likepost(models.Model):
    post= models.ForeignKey(profile,on_delete=models.CASCADE)
    username = models.CharField(max_length=1000)


    def __str__(self):
        return self.username




class webster(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title 

class comment(models.Model):
    post=  models.ForeignKey(profile, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    body = models.TextField()
    Date_added = models.DateTimeField(default= datetime.now(), blank=True)

   
    def __str__(self):
        return '%s -%s' % (self.post.Text, self.name)     



# passowrd = Tomisin
# username = Tomisin




# Create your models here.

