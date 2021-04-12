from django.db import models

class First_player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    

