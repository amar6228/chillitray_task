from django.db import models
from django.db.models.lookups import StartsWith
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    tid=models.AutoField(primary_key=True)
    task_title=models.CharField(max_length=200)
    task_desc=models.TextField()
    task_pic=models.ImageField(upload_to ='uploads/')
    time_stamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Task From: ' + self.tid+ ' , ' +self.uid+ ' , ' +self.task_title


