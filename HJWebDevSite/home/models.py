from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from HJWebDevSite.blocks import Heading_Block, Paragraph_Block, ThreeColumn_Block, Button_Block, GridColumn_BlockCollection, Contact_Block
from home.forms import ContactForm
from django.core import mail
from django.contrib import messages
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.template.response import TemplateResponse

class HomePage(RoutablePageMixin, Page):

    body = StreamField([
        ('heading', Heading_Block()),
        ('paragraph', Paragraph_Block()),
        # ('image', ImageChooser_Block()),
        ('three_column_blocks', ThreeColumn_Block()),
        ('button_block', Button_Block()),
        ('gird_column_block_collection', GridColumn_BlockCollection()),
        ('contact_block', Contact_Block()),
    ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    @route(r'^ajax/$')
    def ajax_view(self, request):
        return TemplateResponse(
          request,
           'home/home_page_ajax.html',
           self.get_context(request)
        )


    def get_context(self, request):
        context = super().get_context(request)

        # TODO: Check if page contains a contact form
        if context['request'].method == "POST":
            contact_form = ContactForm(context['request'].POST)
            if contact_form.is_valid():
                message = "name: "+contact_form.cleaned_data["name"]+'\n'+'email: '+contact_form.cleaned_data["email"]+'\nmessage:\n'+contact_form.cleaned_data["message"]
                messages.add_message(context['request'], messages.SUCCESS, 'Message sent successfully.')
                m = mail.EmailMessage("new mesage from hjwebdev", message, 'noreply@hjwebdev.co.uk', ["hjwebdev@googlemail.com"])
                m.send()

        return context

    class Meta:
        verbose_name = "page"