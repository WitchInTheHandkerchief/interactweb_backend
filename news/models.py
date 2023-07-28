from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(_("Заголовок"), max_length=512)
    date = models.DateField(_("Дата"), auto_now_add=True)
    image = models.ImageField(_("Картинка"), null=True, blank=True)
    content = models.TextField(_("Текст"))

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return f'{self.title}, {self.date}'
