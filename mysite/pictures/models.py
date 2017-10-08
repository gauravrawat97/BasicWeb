from django.db import models

class picture(models.Model):
    title = models.CharField(max_length=10)
    pic = models.ImageField(upload_to = "pictures/static/pictures/pics")
    date = models.DateTimeField()

    def __str__(self):
        return self.title
