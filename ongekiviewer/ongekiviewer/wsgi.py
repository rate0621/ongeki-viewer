"""
WSGI config for ongekiviewer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

## rate add
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ongekiviewer.settings")


application = Cling(get_wsgi_application())
