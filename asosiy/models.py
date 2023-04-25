from django.db import models

class Topic(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Audios(models.Model):
    name = models.CharField(max_length=50)
    location = models.FileField(max_length=100)
    rn = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    size = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    def __str__(self):
        return self.name