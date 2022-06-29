import os

os.environ.setdefault('SECRET_KEY', 'add a security key here')

#Turn on of DEBUG. If True debug wil be On,
#Empty or anything else will be False.

os.environ.setdefault('DEVELOPMENT', 'True')

os.environ.setdefault('DATABASE_URL', 'Database URL')
os.environ.setdefault('ALLOWED_HOSTS', '127.0.0.1 for local development or your app link for online setup')
