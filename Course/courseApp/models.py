from django.db import models


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    ratings = models.IntegerField()

    def __str__(self):
        return self.id + self.name + self.description + self.ratings
