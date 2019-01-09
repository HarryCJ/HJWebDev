from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from HJWebDevSite.blocks import HeadingBlock, ParagraphBlock, ThreeColumnBlock, ButtonBlock, GridColumnBlockCollection, ContactBlock


class HomePage(Page):

    body = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', ParagraphBlock()),
        # ('image', ImageChooserBlock()),
        ('three_column_blocks', ThreeColumnBlock()),
        ('button_block', ButtonBlock()),
        ('gird_column_block_collection', GridColumnBlockCollection()),
        ('contact_block', ContactBlock()),
    ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "page"
