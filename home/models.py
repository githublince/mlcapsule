from django.db import models

# Create your models here.

class cpeoples(models.Model):
    fname = models.CharField(max_length=250,)
    sname = models.CharField(max_length=250,)
    email = models.EmailField(max_length=250,primary_key=True)
    password = models.CharField(max_length=2500)
    
    def getfname(self):
        return self.fname
    def getemail(self):
        return self.email

class userbox(models.Model): # activate required folders for new user
    email = models.ForeignKey(cpeoples, on_delete=models.CASCADE)
    foldername=models.CharField(max_length=250) #username + randomly generated 32 digit keyword

class user_work(models.Model): # After login display work #register new articles here
    id = models.CharField(max_length=2500,primary_key=True)
    email = models.ForeignKey(cpeoples, on_delete=models.CASCADE)
    articletopicname=models.CharField(max_length=1000)
    articlepath=models.CharField(max_length=1000)
    articleimagespath=models.CharField(max_length=1000,default="")


class capinitials(models.Model): #register new articles here
    articleid = models.ForeignKey(user_work, on_delete=models.CASCADE)
    fname = models.CharField(max_length=250,)
    articename=models.CharField(max_length=250)
    viewcount=models.IntegerField(default=0)
    vote=models.IntegerField(default=0)