from django.db import models


# Define your first model from here:
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username
