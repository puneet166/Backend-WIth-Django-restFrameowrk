"""
Django settings for B_W_Django project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x-x&a$63ddxg5lq9jl@6e^m1-+#jy8tzo2bx^tpy8b^@)@70qf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # rest framework
    'rest_framework.authtoken', # token base authenetication after add this run migrate cmd beacuse we want add token field in database user table . after run cmd go admin pannel you will see token field in admin pannel
    # you can create token mannually and assign to any user from django admin pannel
    'Backend', # our APP
    #'knox', # for auth tokenization
    'corsheaders', #app for handling the server headers required for Cross-Origin Resource Sharing (CORS) This is going to be useful when we try to access the API from a different application (React). It helps to connect Django to React.
]
#REST_FRAMEWORK allows both session based and token based authentication. so its permission bases class.
# its for diable all my views for non authenticate User. for acess out view need to authticate first.
# so after add it you cannot  access restframeowrk without authentication 
# so its authenticate for entire system. if you want and put authenetication in specific api view to put like below
# from rest_framework.permission import IsAuthenticated - this line put starting at the view
#@permission_classes([IsAuthtenticated])
# put it before the function body and defination. in api view.

REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES': [
     #   'rest_framework.permissions.IsAuthenticated',
    #],
    # this is for user will authenticate via token.
    'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework.authentication.TokenAuthentication',
    ),
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # its below two middle ware apart of corsheaders APplication
    #They correspond to a filter that’ll intercept all of our application’s requests and apply CORS logic to them.
    'corsheaders.middleware.CorsMiddleware', # add corsheaders middle ware for consum APIS its with corsheaders App

    'django.middleware.common.CommonMiddleware', # same above
]
#add the below to allow which  origins to access the API: so here i am using local host and my API call coming from local host  so i will comment all of them instead of local host
# so this is for if you are API call coming  another url so mention here that URL.but in my case i am using local host..
# why is ?
# becuse if we putted this in here it mean no one can access the API instead jo hmnai mention kiya h ismai ussai chord kr.
CORS_ALLOWED_ORIGINS = [ # it also a part of corsheaders APP
 #   "https://example.com",
  #  "https://sub.example.com",
    "http://localhost:3000",#  API call coming from local host 3000 port beacuse react use 3000 port no 
   # "http://127.0.0.1:9000"
]
#However, since we’re working full localhost, we’ll disable the CORS feature by adding the following
#  its below Parametere apart of corsheaders APplication

#CORS_ORIGIN_ALLOW_ALL = True #And finally, add the line below to allow all origins to access the API:



ROOT_URLCONF = 'B_W_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'B_W_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
