from .base import *

DEBUG = False
SECRET_KEY = 'si9kb2bzbinv$x9ssjqj7salwjwnsz(oru2(nvl6julio9o%6z'
ALLOWED_HOSTS = ["hjwebdev.com", "hjwebdev.co.uk", "www.hjwebdev.com", "www.hjwebdev.co.uk"]

try:
    from .local import *
except ImportError:
    pass
