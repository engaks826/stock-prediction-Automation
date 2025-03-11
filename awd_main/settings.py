from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
########## SECRET_KEY & DEBUG ##########
SECRET_KEY = config('SECRET_KEY')                   
DEBUG = config('DEBUG', default=False, cast=bool)   
ALLOWED_HOSTS = ['*']                               


# Application definition
INSTALLED_APPS = [
    'dal',                               #####
    'dal_select2',                       #####

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',                      #####
    'crispy_bootstrap5',                 #####
    'ckeditor',                          #####
    'anymail',                           #####
    'rest_framework',                    # pip install djangorestframework
    'rest_framework_simplejwt',          # pip install djangorestframework-simplejwt
    'django_filters',                    # pip install django-filter
    'corsheaders',                       # pip install django-cors-headers
    'api',                               #####
    'accounts',                          #####
    'dataentry',                         #####
    'uploads',                           #####
    'emails',                            #####
    'image_compression',                 #####
    'stockanalysis',                     #####
    'blogs',                             #####
]

# Middleware  CONFIGURATION
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", #####
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL  CONFIGURATION
ROOT_URLCONF = 'awd_main.urls'


# Template  CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #####
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


# WSGI application  CONFIGURATION
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


####################  Static files  CONF  ####################
STATIC_URL = 'static/'                                                  
STATIC_ROOT = BASE_DIR / 'static'                                       
STATICFILES_DIRS = [
    'awd_main/static',                                                  
]


####################  Media files  CONF  ####################
MEDIA_URL = '/media/'                                                   
MEDIA_ROOT = BASE_DIR / 'media'                                         


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#################### Messages  CONF    ####################
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',                                        
    50: 'critical',
}

####################   Celery  CONF    ####################
CELERY_BROKER_URL = 'redis://localhost:6379'                          


####################  Default Email  CONF   ####################
DEFAULT_FROM_EMAIL = 'Eng.Aks <infoeng03@gmail.com>'                   
DEFAULT_TO_EMAIL = 'engaks826@gmail.com'   

# # Email CONFIG Using Default Server ((GMAIL SMTP)) Method-1
# EMAIL_HOST = config('EMAIL_HOST')                                     
# EMAIL_PORT = config('EMAIL_PORT', cast=int)                           
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')                           
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')                   
# EMAIL_USE_TLS = True                                                  

# # Email CONFIG Using Brevo Server (Sendinblue) Method-2
EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
ANYMAIL = {
    "SENDINBLUE_API_KEY": config("SENDINBLUE_API_KEY"),
}                            


####################   Crispy forms  CONF    ####################
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap5', 'uni_form', 'bootstrap3', 'bootstrap4', 'semantic-ui')


####################   Ckeditor  CONF   #################### 
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full',
        'height': 100,
    },
}


#####   Ckeditor (Remove Warning text).
SILENCED_SYSTEM_CHECKS = [
    "ckeditor.W001",  # CKEditor 4.22.1 warning
]


####################   Rest-framework  CONF   ####################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', ## use 1st line or this line
    'PAGE_SIZE':2,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'order-by',
}


####################   CORS-Headers CONF  ####################
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5174',
]


####################   NGROK CONF ####################   
CSRF_TRUSTED_ORIGINS = ['https://a026-197-48-200-81.ngrok-free.app']
BASE_URL = 'https://a026-197-48-200-81.ngrok-free.app'







