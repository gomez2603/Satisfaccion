from datetime import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class encuesta(models.Model):
    p1 = models.CharField(max_length=1)
    p2 = models.CharField(max_length=1)
    p3 = models.CharField(max_length=1)
    p4 = models.CharField(max_length=1)
    p5 = models.CharField(max_length=1)
    p6 = models.CharField(max_length=1)
    p7 = models.CharField(max_length=1)
    p8 = models.CharField(max_length=1)
    p9 = models.CharField(max_length=1)
    p10 = models.CharField(max_length=1)
    ob1 = models.CharField(max_length=50)
    ob2 = models.CharField(max_length=50)
    answered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "1.{0} 2.{1} 3.{2} 4.{3} 5.{4} 6.{5} 7.{6} 8.{7} 9.{8} 10.{9} 11.{10} 12.{11}"
        return txt.format(self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.ob1, self.p7, self.p8, self.p9,
                          self.p10, self.ob2)
