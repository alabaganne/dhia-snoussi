from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.subject + ' - ' + self.name