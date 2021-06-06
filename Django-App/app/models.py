from django.db import models

class Coin(models.Model):
	id = models.BigAutoField(primary_key = True)
	name = models.TextField()
	price = models.TextField()

