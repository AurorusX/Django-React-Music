from django.db import models
import string,random
def randomcodegen():
    length=6
    
    while True:
        code=''.join(random.choices(string.ascii_lowercase, k=length))
        if MusicRoom.objects.filter(code=code).count()==0:
            break
    return code
        
# Create your models here.
class MusicRoom(models.Model):
    code=models.CharField(max_length=8,default="",unique=True)
    host=models.CharField(max_length=50,unique=True)
    can_pause=models.BooleanField(null=False,default=False)
    votes_to_skip =models.IntegerField(null=False,default=1)
    created_at =models.DateTimeField(auto_now_add=True)
    
    