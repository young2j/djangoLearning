"""
Django settings for typeidea project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1^)-k5p^op1(j133wpyrr$juu4n2=+199i9_47wxl7y-le4btg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'blog',
    'config',
    'comment',
    'xadmin', #　第三方扩展插件xadmin
    'crispy_forms', #第三方扩展插件xadmin
    'dal', # django-autocomplete-light
    'dal_select2', #django-autocomplete-light
    'ckeditor',
    'ckeditor_uploader',#ckeditor文件上传功能
    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'blog.middleware.user_id.UserIDMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'typeidea.urls'

# THEME = 'default'
THEME = 'bootstrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates', THEME)],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'libraries': {
            #     'comment_block': "comment.templatetags.comment_block"
            # },
        },
    }
]

WSGI_APPLICATION = 'typeidea.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = '/tmp/static/'  # 系统部署上线后的静态资源路径
STATIC_URL = '/static/'  # 静态资源的起始路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates', THEME, 'static')
]


XADMIN_TITLE = 'Typeidea管理后台'
XADMIN_FOOTER_TITLE = 'Powered by django'

"""
-------------------------------------------
ckeditor config
------------------------------------------
"""
CKEDITOR_CONFIGS ={
    'default':{
        'toolbar':'full',
        'height':300,
        'width':850,
        'tabSpaces':4,
        'extraPlugins':'codesnippet',

    }
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
CKEDITOR_UPLOAD_PATH = "article_images"

"""
----------------------------------------------------
自定义文件存储路径
----------------------------------------------------
"""
DEFAULT_FILE_STORAGE = 'typeidea.storage.WatermarkStorage'


"""
----------------------------------------------------
REST_FRAMEWORK配置
----------------------------------------------------
"""
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema', #解决api/docs报错问题
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':2,
}