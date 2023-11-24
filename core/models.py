from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class classes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # s=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    cname=models.CharField(max_length=12)
    roll=models.TextField()
    time=models.DateTimeField(default=now)
    def __str__(self):
        return self.cname
