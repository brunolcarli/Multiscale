from django.db import models


class BattleLogCSV(models.Model):
    data = models.TextField()
    title = models.CharField(max_length=1000, null=False, blank=False)
