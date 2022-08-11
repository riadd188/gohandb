from django.db import models
from django.utils import timezone

# Create your models here.

FACE = (
    (1,'happy'),
    (2,'normal'),
    (3,'danger'),
    (4,'angry')
)
class Item(models.Model):
    place = models.CharField("場所", max_length=100)
    cycle = models.IntegerField("周期")
    cleanup_date = models.DateTimeField("清掃日", default=timezone.now)
    state = models.IntegerField(choices=FACE, default=2)

    def __str__(self):
        return self.place