# DjangoChatChannels
That's a simple chat app that was done using python, django, channels and JS

To run the backend follow these steps:

1) create new empty python environment, for example with conda it would be like:
conda create -n EnvironmentName python
conda activate EnvironmentName
2) run pip install with requirments.txt file which is included in the repository:
pip install -r requirements.txt (You must be in base project folder in promt to do that)
3) make migrations:
python manage.py makemigrations
python manage.py migrate
4) run the server with:
python manage.py runserver (You must be in base project folder in promt to do that)
5) by default server runs on 127.0.0.1:8000, you can browse to that address in
whatever internet browser you use.

The frontend templates for chat are located in /chat/templates/chat folder,
templates for account management are located in /accounts/templates/registration,
and in /static/ folder u may found style.css file.

This project was built using https://channels.readthedocs.io/en/latest/ for some basic templates of
functions to use with Django Channels and https://github.com/justdjango/justchat/ repository for some
templates for authentification process, as well as using templates of chat from https://bootsnipp.com/tags/chat.
For simplicity backend is running with SQLite DB, this can be easily modified in chatsite/settings.py file
