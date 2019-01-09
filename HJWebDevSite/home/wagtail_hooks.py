from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register('insert_global_admin_css')
def editor_css():
	return format_html(
		 '''<link rel="stylesheet" href="{}">''',
        		static('css/admin.css')
    )

