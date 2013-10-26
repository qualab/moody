# -*- coding: utf-8 -*-

from django.db import models

class Mood(models.Model):
    "Настроение пользователя"

    # поля данных
    name = models.CharField(max_length=64, unique=True, db_index=True) # краткое описание настроения
    image = models.ImageField(upload_to='moods', null=True)

    # строковое представление
    def __str__(self):
        return self.name

    # информация для базы данных
    class Meta:
        db_table = 'moods'   # имя таблицы


class Account(models.Model):
    "Аккаунт пользователя"

    # поля данных
    name = models.CharField(max_length=256, unique=True) # идентификатор аккаунта в сети
    mood = models.ForeignKey(Mood, blank=True, null=True) # настроение пользователя

    # строковое представление
    def __str__(self):
        return u"{name} (Настроение: {mood})".format(name=self.name, mood=self.mood.name if self.mood else u'неизвестно')

    # информация для базы данных
    class Meta:
        db_table = 'accounts'   # имя таблицы


class Song(models.Model):
    "Выбранная песня"

    # поля данных
    name = models.CharField(max_length=256, unique=True) # название песни

    # строковое представление
    def __str__(self):
        return self.name

    # информация для базы данных
    class Meta:
        db_table = 'songs'  # имя таблицы


class Selection(models.Model):
    "История выбора"

    # поля данных
    account = models.ForeignKey(Account)            # аккаунт пользователя
    mood    = models.ForeignKey(Mood)               # настроение в момент выбора
    song    = models.ForeignKey(Song)               # одна выбранная песня из списка
    moment  = models.DateTimeField(auto_now=True)   # дата и время выбора

    # строковое представление
    def __str__(self):
        return u'Пользователь: "{account}"; Настроение: {mood}; Песня: "{song}"; "Время: {moment:%d.%m.%y %H:%M:%S}'.format(
                    account=self.account.name,
                    mood=self.mood.name,
                    song=self.song.name,
                    moment=self.moment)

    # информация для базы данных
    class Meta:
        db_table = 'selections' # имя таблицы
        unique_together = [ # уникальное сочетание значений в следующих полях:
            ['account', 'mood', 'song']
        ]


class Rating(models.Model):
    "Оценка песни по настроению"

    # поля данных
    selection   = models.ForeignKey(Selection, unique=True) # выбор песни под настроение пользователем
    rating      = models.IntegerField()                     # оценка песни под определённым настроением

    # строковое представление
    def __str__(self):
        return u'{selection} - Оценка: {rating}'.format(selection=self.selection, rating=self.rating)

    # информация для базы данных
    class Meta:
        db_table = 'ratings' # имя таблицы
