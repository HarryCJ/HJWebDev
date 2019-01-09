# Generated by Django 2.1.5 on 2019-01-08 10:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('three_column_blocks', wagtail.core.blocks.StreamBlock([('heading_1', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_1', wagtail.core.blocks.RichTextBlock()), ('heading_2', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_2', wagtail.core.blocks.RichTextBlock()), ('heading_3', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph_3', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
