from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'dal',                                      #####
    'dal_select2',                              #####

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',                             #####
    'crispy_bootstrap5',                        #####
    'ckeditor',                                 #####
    'anymail',                                  #####
    'rest_framework_simplejwt',                 # pip install djangorestframework-simplejwt                                                     #####
    'rest_framework',                           # pip install djangorestframework
    'django_filters',                           # pip install django-filter
    'corsheaders',                              # pip install django-cors-headers
    'api',                                      #####
    'accounts',                                 #####
    'dataentry',                                #####
    'uploads',                                  #####
    'emails',                                   #####
    'image_compression',                        #####
    'stockanalysis',                            #####
    'blogs',                                    #####
]

# Middleware configuration
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",    #####
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL configuration
ROOT_URLCONF = 'awd_main.urls'


# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],                  #####
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI application configuration
WSGI_APPLICATION = 'awd_main.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files configuration  #####
STATIC_URL = 'static/'                                                  
STATIC_ROOT = BASE_DIR / 'static'                                       
STATICFILES_DIRS = [
    'awd_main/static',                                                  
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media files configuration  #####
MEDIA_URL = '/media/'                                                   
MEDIA_ROOT = BASE_DIR / 'media'                                         


# Messages configuration     #####
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',                                        
    50: 'critical',
}


# Celery configuration    #####
CELERY_BROKER_URL = 'redis://localhost:6379'                          


# # Email configuration Method (1) Using Default ((GMAIL SMTP)) Server  #####
# EMAIL_HOST = config('EMAIL_HOST')                                     
# EMAIL_PORT = config('EMAIL_PORT', cast=int)                           
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')                           
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')                   
# EMAIL_USE_TLS = True                                                  

# Default email configuration   #####
DEFAULT_FROM_EMAIL = 'Eng.Aks <infoeng03@gmail.com>'                   
DEFAULT_TO_EMAIL = 'engaks826@gmail.com'                               


# Crispy forms configuration    #####
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap5', 'uni_form', 'bootstrap3', 'bootstrap4', 'semantic-ui')

CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full',
        'height': 100,
    },
}


# # Email configuration Method (2) Using Sendinblue Server (Brevo)
EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
ANYMAIL = {
    "SENDINBLUE_API_KEY": config("SENDINBLUE_API_KEY"),
}


# # Remove Warning text from ckeditor
SILENCED_SYSTEM_CHECKS = [
    "ckeditor.W001",  # CKEditor 4.22.1 warning
]


# # General Pagination applied on all APIs pages 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':2,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'order-by',
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5174',
]


# every time you restart ngrok app you have to change Forwarding distenation here.
CSRF_TRUSTED_ORIGINS = ['https://06ef-197-48-200-81.ngrok-free.app']
BASE_URL = 'https://06ef-197-48-200-81.ngrok-free.app'







