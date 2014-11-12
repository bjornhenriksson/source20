from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=200, default='Unnamed Url')
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.course_name