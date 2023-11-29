"""
Django settings for CallCenter_SER_Backend project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# 一些隐私配置
from .myconfig import mysql_config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@$n*n91%d7n!^@7-iq-+b0yt=m2x%8we75k4q-d1=eq7h^60w%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   # REST API
    'accounts',         # 自定义用户模型
    'emailbackends',    # 自定义邮箱认证登录
    'corsheaders',      # 跨域库
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域中间件
]

ROOT_URLCONF = 'CallCenter_SER_Backend.urls'

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

WSGI_APPLICATION = 'CallCenter_SER_Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # 修改数据库配置，使用 MySQL
    'default': mysql_config
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 使用自定义的用户模型
AUTH_USER_MODEL = "accounts.CustomUser"

# 自定义认证模型（邮箱登录）
AUTHENTICATION_BACKENDS = [
    # 'django.contrib.auth.backends.ModelBackend',
    'emailbackends.models.CustomModelBackend'
]

# REST API 所有相关的配置
# 全局配置
REST_FRAMEWORK = {
    #指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 自带的分页类
    'PAGE_SIZE': 10,  # 默认每页大小
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',  # 默认时间格式
    'DEFAULT_RENDERER_CLASSES': (  # 默认渲染器 Render 类
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (  # 默认解析器 Parser 类，解析 request.data
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',  # 上传文件
    ),
    'DEFAULT_PERMISSION_CLASSES': [  # 默认权限
        'rest_framework.permissions.IsAuthenticated',  # 必须登录后才能访问
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [  # 默认认证
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # 会话认证
    ]
}

# 关于跨域请求的相关配置
# 跨域支持
CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:5173']  # 授权进行跨站点 HTTP 请求的源列表
# 因为跨域之后需要传递sessionid 到浏览器cookie，所以添加如下配置。
CORS_ALLOW_CREDENTIALS = True  # 允许 Cookie 包含在跨站点 HTTP 请求中
SESSION_COOKIE_SAMESITE = None  # django 自己的安全策略
