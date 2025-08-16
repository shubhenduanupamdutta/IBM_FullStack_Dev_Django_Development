from django.db import models


# Define your first model from here:
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(null=True)

    def __str__(self) -> str:
        return self.username
