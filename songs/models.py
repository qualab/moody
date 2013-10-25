from django.db import models

class Account(models.Model):
    "Аккаунт пользователя"

    # поля данных
    name = models.CharField(max_length=256, unique=True) # идентификатор аккаунта в сети

    # строковое представление
    def __str__(self):
        return self.name

    # информация для базы данных
    class Meta:
        db_table = 'accounts'   # имя таблицы


class Mood(models.Model):
    "Настроение пользователя"

    # поля данных
    name = models.CharField(max_length=64, unique=True) # краткое описание настроения

    # строковое представление
    def __str__(self):
        return self.name

    # информация для базы данных
    class Meta:
        db_table = 'moods'   # имя таблицы


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
    mood    = models.ForeignKey(Mood)               # настроение во время выбора
    song    = models.ForeignKey(Song)               # одна выбранная песня из списка
    moment  = models.DateTimeField(auto_now=True)   # дата и время выбора

    # строковое представление
    def __str__(self):
        return 'Аккаунт: "{account}"; Настроение: "{mood}"; Песня: "{song}"; " + \
                    "Время: {moment:%d.%m.%y %H:%M:%S}'.format(
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
