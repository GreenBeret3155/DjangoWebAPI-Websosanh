# -*- coding: utf-8 -*-
from os import link
from django.db import models
import re

from django.db.models.expressions import Subquery

class KeyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            min_price = models.Min('products__price_sale'),
        )

class Key(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    transformed_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    link_img = models.CharField(max_length=50)
    Ram = models.CharField(max_length=10)
    Bonhotrong = models.CharField(max_length=50)
    Pin = models.CharField(max_length=50)

    #use Manager() to custom query
    objects = KeyManager()

    # @property
    # def transformed_name(self):
    #     INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"

    #     OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"

    #     r = re.compile("|".join(INTAB))
    #     replaces_dict = dict(zip(INTAB, OUTTAB))

    #     def khongdau(utf8_str):
    #         return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
    #     return khongdau(self.name)

    # def __str__(self):
    #     return self.name



class Noi_ban(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    link_img = models.CharField(max_length=100, null=True, blank=True)
    price_sale = models.IntegerField()
    price_goc = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    manhinh = models.CharField(max_length=50, null=True, blank=True)
    hedieuhanh = models.CharField(max_length=50, null=True, blank=True)
    cameratruoc = models.CharField(max_length=20, null=True, blank=True)
    CPU = models.CharField(max_length=50, null=True, blank=True)
    Ram = models.CharField(max_length=10, null=True, blank=True)
    Bonhotrong = models.CharField(max_length=50, null=True, blank=True)
    Pin = models.CharField(max_length=50, null=True, blank=True)
    noi_ban = models.ForeignKey(
        Noi_ban,
        db_column= 'id_noiban',
        on_delete=models.CASCADE,
    )
    key = models.ForeignKey(
        Key,
        related_name = 'products',
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.name