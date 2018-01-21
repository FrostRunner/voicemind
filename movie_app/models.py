#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born = models.DateField()

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Movie(models.Model):
    # color = models.CharField(max_length=256, default="")
    # director_name = models.CharField(max_length=256, default="")
    # num_critic_for_reviews = models.IntegerField()
    # duration = models.CharField(max_length=256, default="")
    # director_facebook_likes = models.CharField(max_length=256, default="")
    # actor_3_facebook_likes = models.CharField(max_length=256, default="")
    # actor_2_name = models.CharField(max_length=256, default="")
    # actor_1_facebook_likes = models.CharField(max_length=256, default="")
    # gross = models.CharField(max_length=256, default="")
    # genres = models.CharField(max_length=256, default="")
    # actor_1_name = models.CharField(max_length=256, default="")
    # movie_title = models.CharField(max_length=256, default="")
    # num_voted_users = models.CharField(max_length=256, default="")
    # cast_total_facebook_likes = models.CharField(max_length=256, default="")
    # actor_3_name = models.CharField(max_length=256, default="")
    # facenumber_in_poster = models.CharField(max_length=256, default="")
    # plot_keywords = models.CharField(max_length=256, default="")
    # movie_imdb_link = models.CharField(max_length=256, default="")
    # num_user_for_reviews = models.CharField(max_length=256, default="")
    # language = models.CharField(max_length=256, default="")
    # country = models.CharField(max_length=256, default="")
    # content_rating = models.CharField(max_length=256, default="")
    # budget = models.CharField(max_length=256, default="")
    # title_year = models.CharField(max_length=256, default="")
    # actor_2_facebook_likes = models.CharField(max_length=256, default="")
    # imdb_score = models.CharField(max_length=256, default="")
    # aspect_ratio = models.CharField(max_length=256, default="")
    # movie_facebook_likes = models.CharField(max_length=256, default="")
    poster = models.ImageField(upload_to="movie/{}/poster/".format(id(object)),
                               default="movie/default/poster/default.png")
    trailer = models.CharField(max_length=255, null=True, blank=True,
                               default="/media/movie/default/trailer/default.mp4")
    added_at = models.CharField(max_length=256, default="")
    blocked_at = models.BooleanField(default=False)
    block_ru = models.BooleanField(default=False)
    block_ua = models.BooleanField(default=False)
    camrip = models.CharField(max_length=256, default="")
    category = models.CharField(max_length=256, default="")
    iframe_url = models.CharField(max_length=256, default="")
    instream_ads = models.CharField(max_length=256, default="")
    kinopoisk_id = models.CharField(max_length=256, default="")
    pornolab_id = models.CharField(max_length=256, default="")
    title_en = models.CharField(max_length=256, default="")
    title_ru = models.CharField(max_length=256, default="")
    token = models.CharField(max_length=256, default="")
    translator = models.CharField(max_length=256, default="")
    translator_id = models.CharField(max_length=256, default="")
    type = models.CharField(max_length=256, default="")
    world_art_id = models.CharField(max_length=256, default="")
    genres = models.CharField(max_length=256, default="Action")
    country = models.CharField(max_length=256, default="USA")





    def __str__(self):
        return self.title_en

    @property
    def genre_list(self):
        return self.genres.split(",")

    @property
    def get_poster_upload_folder(self):
        return "movie/{}/poster/".format(self.id)
    #
    # def genres_list(self):
    #     return self.genres.split("|")
    #
    def put_poster(self):
        models.ImageField(upload_to=self.get_poster_upload_folder,
                          default="movie/default/poster/default.png")

    class Meta:
        # ordering = ["-project", "summary"]
        # unique_together = ("project", "summary", "project")
        # verbose_name = "задача"
        # verbose_name_plural = "задачи"
        pass
