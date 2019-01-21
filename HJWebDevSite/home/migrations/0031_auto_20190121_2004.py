# Generated by Django 2.1.5 on 2019-01-21 20:04

import HJWebDevSite.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20190119_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('heading', wagtail.core.blocks.CharBlock(classname='full title'))])), ('paragraph', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('alignment_mobile', wagtail.core.blocks.ChoiceBlock(choices=[('col-xs-alignment-left', 'Left'), ('col-xs-alignment-center', 'Centre'), ('col-xs-alignment-right', 'Right')])), ('alignment_tablet', wagtail.core.blocks.ChoiceBlock(choices=[('col-sm-alignment-left', 'Left'), ('col-sm-alignment-center', 'Centre'), ('col-sm-alignment-right', 'Right')])), ('alignment_desktop', wagtail.core.blocks.ChoiceBlock(choices=[('col-md-alignment-left', 'Left'), ('col-md-alignment-center', 'Centre'), ('col-md-alignment-right', 'Right')])), ('text', wagtail.core.blocks.RichTextBlock())])), ('three_column_blocks', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('heading_1', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_1', wagtail.core.blocks.RichTextBlock()), ('heading_2', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_2', wagtail.core.blocks.RichTextBlock()), ('heading_3', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_3', wagtail.core.blocks.RichTextBlock())])), ('button_block', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('text', wagtail.core.blocks.CharBlock()), ('page', HJWebDevSite.blocks.PageChooserBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(False))])), ('gird_column_block_collection', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('gridColumnBlock', wagtail.core.blocks.StreamBlock([('grid_column_block', wagtail.core.blocks.StructBlock([('grid_proportion_mobile', wagtail.core.blocks.ChoiceBlock(choices=[('hidden-xs', 'Hidden'), ('col-xs-1', '1'), ('col-xs-2', '2'), ('col-xs-3', '3'), ('col-xs-4', '4'), ('col-xs-5', '5'), ('col-xs-6', '6'), ('col-xs-7', '7'), ('col-xs-8', '8'), ('col-xs-9', '9'), ('col-xs-10', '10'), ('col-xs-11', '11'), ('col-xs-12', '12')])), ('grid_proportion_tablet', wagtail.core.blocks.ChoiceBlock(choices=[('hidden-sm', 'Hidden'), ('col-sm-1', '1'), ('col-sm-2', '2'), ('col-sm-3', '3'), ('col-sm-4', '4'), ('col-sm-5', '5'), ('col-sm-6', '6'), ('col-sm-7', '7'), ('col-sm-8', '8'), ('col-sm-9', '9'), ('col-sm-10', '10'), ('col-sm-11', '11'), ('col-sm-12', '12')])), ('grid_proportion_desktop', wagtail.core.blocks.ChoiceBlock(choices=[('hidden-md hidden-lg', 'Hidden'), ('col-md-1', '1'), ('col-md-2', '2'), ('col-md-3', '3'), ('col-md-4', '4'), ('col-md-5', '5'), ('col-md-6', '6'), ('col-md-7', '7'), ('col-md-8', '8'), ('col-md-9', '9'), ('col-md-10', '10'), ('col-md-11', '11'), ('col-md-12', '12')])), ('alignment_mobile', wagtail.core.blocks.ChoiceBlock(choices=[('col-xs-alignment-left', 'Left'), ('col-xs-alignment-center', 'Centre'), ('col-xs-alignment-right', 'Right')])), ('alignment_tablet', wagtail.core.blocks.ChoiceBlock(choices=[('col-sm-alignment-left', 'Left'), ('col-sm-alignment-center', 'Centre'), ('col-sm-alignment-right', 'Right')])), ('alignment_desktop', wagtail.core.blocks.ChoiceBlock(choices=[('col-md-alignment-left', 'Left'), ('col-md-alignment-center', 'Centre'), ('col-md-alignment-right', 'Right')])), ('content', wagtail.core.blocks.RichTextBlock()), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False))]))]))])), ('contact_block', wagtail.core.blocks.StructBlock([('padding_top', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('padding_bottom', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('background_style', wagtail.core.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark'), ('sand', 'Sand'), ('water', 'Water')])), ('extra_options', wagtail.core.blocks.StreamBlock([('makeBlockLink', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock())]))], required=False)), ('send_email', wagtail.core.blocks.EmailBlock(default='hjwebdev@googlemail.com', label='Address to which the contact form sends an email.'))]))], blank=True, null=True),
        ),
    ]