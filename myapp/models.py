from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
