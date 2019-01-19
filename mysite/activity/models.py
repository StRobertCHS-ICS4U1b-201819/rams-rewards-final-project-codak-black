from django.db import models


class Points(models.Model):
    name = models.CharField(max_length=140)
    activity = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


