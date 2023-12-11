from django.db import models

class Medicine(models.Model):
    code = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    quantity = models.IntegerField()

    def __str__ (self):
        return self.name