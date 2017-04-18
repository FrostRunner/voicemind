#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.IntegerField()

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s

    def get_in_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"
