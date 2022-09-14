from email.mime import image
from email.policy import default
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Image(models.Model):

    origin = models.ImageField(upload_to="photos/%y/%m/%d/")

    big = ImageSpecField(source="origin",
                         processors=[ResizeToFill(1280, 1024)],
                         format='JPEG'
                         )

    thumbnail = ImageSpecField(source='origin',
                            processors=[ResizeToFill(250,250)],
                            format="JPEG",
                            options={'quality': 60}
                            )

    middle = ImageSpecField(source='origin',
                        processors=[ResizeToFill(600, 400)],
                        format="JPEG",
                        options={'quality': 75}
                        )

    small = ImageSpecField(source='origin',
                            processors=[ResizeToFill(75,75)],
                            format="JPEG",
                            options={'quality': 50}
                            )
                            
PLACES = (
    (1, '和食'),
    (2, '中華'),
    (3, '洋食'),
    (4, 'ジャンク'),
    (5, 'おやつ'),
    (6, 'その他'),
)

class Item(models.Model):
    registerer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField("料理名", max_length=100)
    place = models.IntegerField(choices=PLACES)
    need = models.BooleanField(verbose_name='補充が必要か',  default=False)
    memo = models.TextField("メモ", blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)
    image = models.ImageField(default='default.jpg', blank =True)

    def __str__(self):
        return self.item


# Create your models here.
