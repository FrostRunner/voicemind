#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page.models import Category, Good
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import InvalidPage, Paginator


def index(request, id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=id)
    paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 3)
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    # goods = Good.objects.filter(category=cat).order_by("name")
    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods})


def good(request, id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=id)
    except Good.DoesNotExist:
        raise Http404
    return render(request, "good.html", {"cats": cats, "good": good, "pn": page_num})


def category(request, id):
    try:
        category = Good.objects.get(pk=id)
    except:
        raise Http404
    s = category.name + "<br><br>" + category.description
    return HttpResponse(s)
