from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Progress(models.Model):
    user = models.ForeignKey(User, unique=True)
    course_name = models.ForeignKey('get_class.Course')
    progress = models.IntegerField(default=0)
    def __int__(self):
        return self.progress

