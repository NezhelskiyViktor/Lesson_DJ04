from django.db import models


class Film_post(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    description = models.TextField('Описание фильма')
    text = models.TextField('Отзыв о фильме')

    def __str__(self):
        return self.title
    class Meta:
            verbose_name = 'Фильм'
            verbose_name_plural = 'Фильмы'
