from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    age = models.IntegerField()
    image = models.ImageField(upload_to='dogs/', null=True, blank=True)

    def __str__(self):
        return self.name
