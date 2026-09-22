from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    srno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    data=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default = False)

    def __str__(self):
        return self.title
      