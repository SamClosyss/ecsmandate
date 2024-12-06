from django.db import models

# Create your models here.


class Ocr(models.Model):
    umrn_no = models.IntegerField(default=0)
