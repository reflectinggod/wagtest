from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class HomePage(Page):
    # поля в БД
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Подзаголовок'
    )
    rtfbody = RichTextField(
        blank=True,
        null=True
    )
    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # поля в админке
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
        ImageChooserPanel('bg_image')
    ]