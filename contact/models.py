from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)  # Optional field
    address = models.TextField(blank=True)  # Optional field
    message = models.TextField()

    def __str__(self):
        return self.name
