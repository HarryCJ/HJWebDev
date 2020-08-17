from django.db import models

# Create your models here.
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import RawHTMLBlock
from HJWebDevSite.blocks import Heading_Block, Paragraph_Block, ThreeColumn_Block, Button_Block, GridColumn_BlockCollection, Contact_Block
from home.forms import ContactForm
from django.core import mail
from django.contrib import messages
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.template.response import TemplateResponse

class HTMLPage(RoutablePageMixin, Page):

    body = StreamField([
        ('page_content', RawHTMLBlock(required=True)),
    ], null=True, blank=True)

    # page_content = RawHTMLBlock(required=True)
    # StreamField([
    #     ('heading', Heading_Block()),
    #     ('paragraph', Paragraph_Block()),
    #     # ('image', ImageChooser_Block()),
    #     ('three_column_blocks', ThreeColumn_Block()),
    #     ('button_block', Button_Block()),
    #     ('gird_column_block_collection', GridColumn_BlockCollection()),
    #     ('contact_block', Contact_Block()),
    # ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    # @route(r'^ajax/$')
    # def ajax_view(self, request):
    #     return TemplateResponse(
    #       request,
    #        'home/home_page_ajax.html',
    #        self.get_context(request)
    #     )


    # def get_context(self, request):
    #     context = super().get_context(request)
    #     return context

    # class Meta:
    #     verbose_name = "page"