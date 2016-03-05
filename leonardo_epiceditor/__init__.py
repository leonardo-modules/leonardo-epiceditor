
from django.apps import AppConfig

default_app_config = 'leonardo_epiceditor.Config'


LEONARDO_APPS = ['leonardo_epiceditor']
LEONARDO_JS_FILES = ['lib/js/epiceditor.init.js']


LEONARDO_OPTGROUP = 'EpicEditor'

LEONARDO_CONFIG = {
    'LEONARDO_EPICEDITOR_PUBLIC': (True, 'Make epiceditor view accessible without login.'),
}


class Config(AppConfig):
    name = 'leonardo_epiceditor'
    verbose_name = "leonardo-epiceditor"
