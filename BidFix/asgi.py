# mysite/asgi.py

import os

from django.core.wsgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BidFix.settings')

application = get_asgi_application()