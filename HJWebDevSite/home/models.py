from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from HJWebDevSite.blocks import HeadingBlock, ParagraphBlock, ThreeColumnBlock, ButtonBlock, GridColumnBlockCollection, ContactBlock
from home.forms import ContactForm
from django.core import mail
from django.contrib import messages


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
