from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    def __str__(self):
        return self.course_name

class GetUrl(models.Model):
    current_course = models.ForeignKey(Course)
    url_name = models.CharField(max_length=200, default='Unnamed Url')
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.url_name
