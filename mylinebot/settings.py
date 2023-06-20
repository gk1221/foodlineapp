"""
Django settings for mylinebot project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LINE_CHANNEL_ACCESS_TOKEN = "JC4AWZ7AGnx3MQZ5+vo4TIEluPZtK8Nx5crykdbf32GtxHZXKkbCaKhf2IUMnBVRGDl2hCWZYYT4MdjPi8DdC54BoCE6WXWABBfw5P0s468EGaiXCP+d9DZ8QIdjuq5Ky/9wuhbc6nfeAfPBsgdPwwdB04t89/1O/w1cDnyilFU="

LINE_CHANNEL_SECRET = "1b6796cf9312b195ddcfa24603dd26f3"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qua56p&ht)sx!uq15^)4g3o3%p-qe)^23xa+ar=+h7yvbka=a("


ALLOWED_HOSTS = [
    "foodielinebotzxcv.herokuapp.com",
    "176e-123-193-9-28.ngrok.io",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    "ckeditor_uploader",
    "foodlinebot.apps.FoodlinebotConfig",
    "roombot.apps.RoombotConfig",
    "rest_framework",
    'news',
    'django_extensions',
    'corsheaders',
   
]

REST_FRAMEWORK = {
    "PAGE_SIZE": 100,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

]



ROOT_URLCONF = "mylinebot.urls"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mylinebot.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # PostgreSQL
        "NAME": "dcic31cfoangh2",  # 資料庫名稱
        "USER": "lqhjmhstejawac",  # 資料庫帳號
        "PASSWORD": "f7ba05eefe1631c86e151f9b8c851348faf6d0677f7b378b014ea175256d258a",  # 資料庫密碼
        "HOST": "ec2-34-225-167-77.compute-1.amazonaws.com",  # Server(伺服器)位址
        "PORT": "5432",  # PostgreSQL Port號
    },
}
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # PostgreSQL
        "NAME": "linebot",  # 資料庫名稱
        "USER": "postgres",  # 資料庫帳號
        "PASSWORD": "zxcv125628",  # 資料庫密碼
        "HOST": "localhost",  # Server(伺服器)位址
        "PORT": "5432",  # PostgreSQL Port號
    },
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "zh-Hant"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)22222
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
# STATIC_ROOT = os.path.join(BASE_DIR,'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


CKEDITOR_JQUERY_URL = "https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_CONFIGS = {
    # 配置名是default時，django-ckeditor預設使用這個配置
    "default": {
        # 使用簡體中文
        #: ["body {font-size: 18px;font-family:'Comic Sans MS';}"],
        "skin": "n1theme",
        # 'uiColor': '#FFD7C8',
        "language": "zh-cn",
        # 編輯器的寬高請根據你的頁面自行設定
        "width": "730px",
        "height": "500px",
        "image_previewText": " ",
        "tabSpaces": 2,
        "toolbar": "None",
        # 新增按鈕在這裡
        # 外掛
        "extraPlugins": ",".join(
            [
                "prism",
                "codesnippet",
                "uploadimage",
                "widget",
                "lineutils",
            ]
        ),
    }
}


customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEBUG = True