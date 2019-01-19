from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class ExtraOptions_Block(blocks.StructBlock):

    eo_type = ""

    @property
    def get_eo_classes(self):
        return "test classes"

    @property
    def get_eo_start(self):
        return "test start"

    @property
    def get_eo_end(self):
        return "test end"

class MakeBlockLink_Block(ExtraOptions_Block):

    eo_type = "make_block_link"

    link = blocks.CharBlock()

    # make_block_link = blocks.ChoiceBlock(choices=[
    #     (True, 'Yes'),
    #     (False, 'No'),
    # ], default=True)

    # @property
    # def get_eo_start(self):
    #     # print("self.__dict__")
    #     # print(self.__dict__)
    #     # print('self.child_blocks.values()')
    #     # print(self.child_blocks.values())
    #     # for cb in self.child_blocks.values():
    #     #     print("""cb.value""")
    #     #     print(cb.value)
    #     if self.child_blocks["make_block_link"] == True:
    #         return "start link"
    #     else:
    #         return ""

    # @property
    # def get_eo_classes(self):
    #     if self.child_blocks["make_block_link"] == True:
    #         return "make-block-link"
    #     else:
    #         return ""
    
    # @property
    # def get_eo_end(self):
    #     if self.child_blocks["make_block_link"] == True:
    #         return "end link"
    #     else:
    #         return ""

    class Meta:
        template = 'blocks/extra_options/make_block_link.html'
        icon = 'link'

class Generic_Block(blocks.StructBlock):

    padding_top = blocks.ChoiceBlock(choices=[
        ('none', 'None'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], default='medium')

    padding_bottom = blocks.ChoiceBlock(choices=[
        ('none', 'None'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ],  default='medium')

    background_color = blocks.ChoiceBlock(choices=[
        ('light', 'Light'),
        ('dark', 'Dark'),
    ],  default='light')

    extra_options = blocks.StreamBlock([
        ('makeBlockLink', MakeBlockLink_Block()),
        ], 
        required=False)

# class ExtraOptions_Block(blocks.StructBlock):

    # mobile_padding_top = blocks.ChoiceBlock(choices=[
    #     ('none', 'None'),
    #     ('small', 'Small'),
    #     ('medium', 'Medium'),
    #     ('large', 'Large'),
    # ], default='medium')

    # mobile_padding_bottom = blocks.ChoiceBlock(choices=[
    #     ('none', 'None'),
    #     ('small', 'Small'),
    #     ('medium', 'Medium'),
    #     ('large', 'Large'),
    # ],  default='medium')

    # class Meta:
    #     template = 'blocks/extra_options/mobile_padding_block.html'

class ThreeColumn_Block(Generic_Block):
    # title = blocks.CharBlock(classname="full title")
    heading_1 = blocks.CharBlock(classname="full title")
    paragraph_1 = blocks.RichTextBlock()
    heading_2 = blocks.CharBlock(classname="full title")
    paragraph_2 = blocks.RichTextBlock()
    heading_3 = blocks.CharBlock(classname="full title")
    paragraph_3 = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/three_column_block.html'
        icon = 'placeholder'

class Heading_Block(Generic_Block):

    heading = blocks.CharBlock(classname="full title")

    class Meta:
        template = 'blocks/heading_block.html'
        icon = 'title'

class Paragraph_Block(Generic_Block):

    alignment_mobile = blocks.ChoiceBlock(choices=[
        ('col-xs-alignment-left', 'Left'),
        ('col-xs-alignment-center', 'Centre'),
        ('col-xs-alignment-right', 'Right'),
    ],  default='col-xs-alignment-left')
    alignment_tablet = blocks.ChoiceBlock(choices=[
        ('col-sm-alignment-left', 'Left'),
        ('col-sm-alignment-center', 'Centre'),
        ('col-sm-alignment-right', 'Right'),
    ],  default='col-sm-alignment-left')
    alignment_desktop = blocks.ChoiceBlock(choices=[
        ('col-md-alignment-left', 'Left'),
        ('col-md-alignment-center', 'Centre'),
        ('col-md-alignment-right', 'Right'),
    ],  default='col-md-alignment-left')
    text = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/paragraph_block.html'
        form_template ="blocks/paragraph_block_admin.html"
        icon = 'pilcrow'

class Button_Block(Generic_Block):

    text = blocks.CharBlock()
    url = blocks.CharBlock()

    class Meta:
        template = 'blocks/button_block.html'
        icon = 'link'

class Contact_Block(Generic_Block):

    send_email = blocks.EmailBlock(default="hjwebdev@googlemail.com", label="Address to which the contact form sends an email.")

    class Meta:
        template = 'blocks/contact_block.html'
        icon = 'mail'

class GridColumn_Block(blocks.StructBlock):

    grid_proportion_mobile = blocks.ChoiceBlock(choices=[ ('hidden-xs', 'Hidden'), 
        ('col-xs-1', '1'), ('col-xs-2', '2'), ('col-xs-3', '3'),
        ('col-xs-4', '4'), ('col-xs-5', '5'), ('col-xs-6', '6'),
        ('col-xs-7', '7'), ('col-xs-8', '8'), ('col-xs-9', '9'),
        ('col-xs-10', '10'), ('col-xs-11', '11'), ('col-xs-12', '12'),
    ],  default='col-xs-12')
    grid_proportion_tablet = blocks.ChoiceBlock(choices=[ ('hidden-sm', 'Hidden'), 
        ('col-sm-1', '1'), ('col-sm-2', '2'), ('col-sm-3', '3'),
        ('col-sm-4', '4'), ('col-sm-5', '5'), ('col-sm-6', '6'),
        ('col-sm-7', '7'), ('col-sm-8', '8'), ('col-sm-9', '9'),
        ('col-sm-10', '10'), ('col-sm-11', '11'), ('col-sm-12', '12'),
    ],  default='col-sm-6')
    grid_proportion_desktop = blocks.ChoiceBlock(choices=[ ('hidden-md hidden-lg', 'Hidden'), 
        ('col-md-1', '1'), ('col-md-2', '2'), ('col-md-3', '3'),
        ('col-md-4', '4'), ('col-md-5', '5'), ('col-md-6', '6'),
        ('col-md-7', '7'), ('col-md-8', '8'), ('col-md-9', '9'),
        ('col-md-10', '10'), ('col-md-11', '11'), ('col-md-12', '12'),
    ],  default='col-md-6')

    alignment_mobile = blocks.ChoiceBlock(choices=[
        ('col-xs-alignment-left', 'Left'),
        ('col-xs-alignment-center', 'Centre'),
        ('col-xs-alignment-right', 'Right'),
    ],  default='col-xs-alignment-left')
    alignment_tablet = blocks.ChoiceBlock(choices=[
        ('col-sm-alignment-left', 'Left'),
        ('col-sm-alignment-center', 'Centre'),
        ('col-sm-alignment-right', 'Right'),
    ],  default='col-sm-alignment-left')
    alignment_desktop = blocks.ChoiceBlock(choices=[
        ('col-md-alignment-left', 'Left'),
        ('col-md-alignment-center', 'Centre'),
        ('col-md-alignment-right', 'Right'),
    ],  default='col-md-alignment-left')

    content = blocks.RichTextBlock()

    extra_options = blocks.StreamBlock([
        ('makeBlockLink', MakeBlockLink_Block()),
        ], 
        required=False)

    # def get_form_context(self, value, prefix='', errors=None):

    #     # print (value)
    #     # for key, value2 in value.items(): 
    #     #     print(key, value2)

    #     # print(value["grid_proportion_mobile"])

    #     # if "grid_proportion_mobile" in value.keys(): 
    #     #     print("Present, ", end =" ") 
    #     #     print("value =", value["grid_proportion_mobile"]) 
    #     # else: 
    #     #     print("Not present") 

    #     context = super(GridColumnBlock, self).get_form_context(value, prefix=prefix, errors=errors)
    #     return context

    class Meta:
        template = 'blocks/grid_column_block.html'
        form_template ="blocks/grid_column_block_admin.html"
        icon='placeholder'

class GridColumn_BlockCollection(Generic_Block):

    gridColumnBlock = blocks.StreamBlock([
        ('grid_column_block', GridColumn_Block()),])

    class Meta:
        template = 'blocks/grid_column_block_collection.html'
        icon='placeholder'