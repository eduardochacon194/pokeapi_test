from django.db import models

class pokeapi(models.Model):
    name_poke = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_poke