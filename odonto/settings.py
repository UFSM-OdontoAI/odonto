from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'odonto-dev'
DEBUG = False
ALLOWED_HOSTS = ["localhost","127.0.0.1","200.132.35.11"]
FORCE_SCRIPT_NAME = "/odonto"
INSTALLED_APPS = [
 'django.contrib.staticfiles',
 'viewer',
]
MIDDLEWARE = []
ROOT_URLCONF = 'odonto.urls'
TEMPLATES = [{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[BASE_DIR/'viewer/templates'],
 'APP_DIRS':True,
 'OPTIONS':{'context_processors':[]},
}]
WSGI_APPLICATION = 'odonto.wsgi.application'
STATIC_URL = '/odonto/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR/'viewer/static']
COCO_DATASETS = {
 'train': {
  'images': BASE_DIR/'data/train2017',
  'annotations': BASE_DIR/'data/annotations/instances_train2017.json'
 },
 'val': {
  'images': BASE_DIR/'data/val2017',
  'annotations': BASE_DIR/'data/annotations/instances_val2017.json'
 }
}
