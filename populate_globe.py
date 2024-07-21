import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'globetrotters.settings')


import django
django.setup()
from globe_app.models import *

def populate():
    pass
    # destinations = [
    #     {'location':'Iceland'}
    #     {'location':'Norway'}
    #     {'location':'Finland'}
    #     ]
