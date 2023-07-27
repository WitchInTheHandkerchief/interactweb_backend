from django.db import models
from django.utils.translation import gettext_lazy as _


class Form(models.Model):
    name = models.CharField(_("Имя"), max_length=128)
    date_of_birth = models.DateField(_("Дата рождения"))
    phone_number = models.CharField(_("Номер телефона"), max_length=64)

    class Meta:
        verbose_name = _("form")
        verbose_name_plural = _("forms")

    def __str__(self):
        return f'{self.name}'

