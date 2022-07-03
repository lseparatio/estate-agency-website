import os

os.environ.setdefault('SECRET_KEY', 'add a security key here')

# Turn on of DEBUG. If True debug wil be On,
# Empty or anything else will be False.

os.environ.setdefault('DEVELOPMENT', 'True')

os.environ.setdefault('DATABASE_URL', 'Database URL')
os.environ.setdefault(
    'ALLOWED_HOSTS', '127.0.0.1 for local development or your app link for online setup')

# Rechapcha keys: https://www.google.com/recaptcha/

os.environ.setdefault('RECAPTCHA_PUBLIC_KEY', 'Your public key')
os.environ.setdefault('RECAPTCHA_PRIVATE_KEY', 'Your private key')

# Email settings

os.environ.setdefault('DEFAULT_FROM_EMAIL', 'Default sending email')
os.environ.setdefault('EMAIL_USE_TLS', 'True')
os.environ.setdefault('PORT', '465')
os.environ.setdefault('EMAIL_HOST', 'Your email host')
os.environ.setdefault('EMAIL_HOST_USER', 'Your email user')
os.environ.setdefault('EMAIL_HOST_PASSWORD', 'Your email password')
