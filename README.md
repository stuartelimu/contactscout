# Class Based Views

This is a phone book application that allows users to store telephone numbers along with email addresses and images for friends and family.

This project serves as a basic introduction to djago's class based views which I cover in this [article]()

#### Project setup
Clone or download this repository to a location on your machine. Change into the `contactscout` directory with the following commad.

```
cd contactscout
```

Create and activate a virtual environment.

```
virtualenv env && source env/bin/activate
```

Install the packages from the requirements file

```
pip install -r requirements.txt
```

Generate a new secret key for your django project.

```
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
Copy the generated key to your settings file

We can now make migrations to create our database. In the terminal type the following commands

```
./manage.py makemigrations

./manage.py migrate
```

Once that's done you can start the development server.

```
./manage.py runserver
```

The project already contains an accounts app which will be used for handling user accounts.

You can try to register and login 

