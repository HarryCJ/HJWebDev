from datetime import date
from django import template
from django.conf import settings
from django import forms

# from plainpage.models import PlainPage
# from home.models import HomePage
from wagtail.core.models import Page
# from siteoptions.models import SiteOptions

register = template.Library()

class ContactForm(forms.Form):
        
    name = forms.CharField(label='Your name:', max_length=100)
    email = forms.CharField(label='Your email:', max_length=100)
    message = forms.CharField(label='Your message:', max_length=500, widget=forms.Textarea)

@register.simple_tag(takes_context=True)
def get_contact_form(context):

	contact_form = ContactForm()

	if context['request'].method == "POST":
		contact_form = ContactForm(context['request'].POST)
		if contact_form.is_valid():
			message = "name: "+contact_form.cleaned_data["name"]+'\n'+'email: '+contact_form.cleaned_data["email"]+'\nmessage:\n'+contact_form.cleaned_data["message"]
			m = mail.EmailMessage("new mesage from hjwebdev", message, 'noreply@hjwebdev.co.uk', ["hjwebdev@googlemail.com"])
			m.send()

	return contact_form

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page

# @register.assignment_tag(takes_context=True)
# def get_contact_details(context):
#     # NB this returns a core.Page, not the implementation-specific model used
#     # so object-comparison to self will return false as objects would differ

#     return SiteOptions.for_site(context['request'].site)


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live()#.in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves all live pages which are children of the calling page
#for standard index listing
@register.inclusion_tag(
    'standard_index_listing.html',
    takes_context=True
)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live()
    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }