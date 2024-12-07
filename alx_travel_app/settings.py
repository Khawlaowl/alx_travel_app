import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='3306'),
    }
}


INSTALLED_APPS = [
    # other apps...
    'rest_framework',
    'corsheaders',
    'listings',  # Add your listings app here
]

MIDDLEWARE = [
    # other middleware...
    'corsheaders.middleware.CorsMiddleware',
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Add your front-end URL
]
