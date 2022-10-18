Recommended to use Python version > 3.9


See the ENGINE setting below on how to specify other database types. This example is for PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


Activate environment using this command;
conda activate <env_name>


To install dependencies:
pip install -r requirements.txt

Then run below commands:
#to make migrations:
python manage.py makemigrations

#to apply migrations;
python manage.py migrate

#to runserver:
pyhton manage.py runserver