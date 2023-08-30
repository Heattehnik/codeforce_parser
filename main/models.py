from django.db import models


class Theme(models.Model):
    theme = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.theme


class Problem(models.Model):
    contest_id = models.IntegerField(verbose_name='Порядковый номер')
    index = models.CharField(max_length=10, verbose_name='Индекс')
    title = models.CharField(max_length=150, verbose_name='Название')
    theme = models.ManyToManyField(
                                Theme,
                                blank=True,
                                null=True,
                                verbose_name='Тема',
                                related_name='problem'
                                )
    solve_count = models.PositiveIntegerField(verbose_name='Раз решено')
    difficulty = models.PositiveIntegerField(verbose_name='Сложность', null=True, blank=True)

    def __str__(self):
        return self.title





