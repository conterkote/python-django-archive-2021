from django.db import models

# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.topic

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

class UsersBase(models.Model):
    username = models.CharField(max_length = 264)
    email = models.EmailField()
    password = models.CharField(max_length = 264)

    def __str__(self):
        return str("Username: " + self.username + "; E-mail: " + self.email + "; Password: " + self.password)