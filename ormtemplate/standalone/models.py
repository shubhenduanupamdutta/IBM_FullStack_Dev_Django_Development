from django.db import models  # noqa: D100, INP001


# Test model
class Test(models.Model):  # noqa: D101
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self) -> str:  # noqa: D105
        return self.name