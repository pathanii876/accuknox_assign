from django.db import models


# Created mymodel with receiver function

class SyncModel(models.Model):
    name = models.CharField(max_length=50)


class TransModel(models.Model):
    name = models.CharField(max_length=100)


