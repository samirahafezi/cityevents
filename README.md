# CityEvents 🎉

## Local environment setup

In this setup I'm using VSCode and Postgresdb.

1) Install Pipenv:

```
pip3 install pipenv
```

2) Install Django in the virtual environment inside the directory (this isn't a global virtual environment):

```
pipenv install django
```

```
python pipenv shell
```
<br>

**If you're pulling the GitHub repo, you can skip steps 3 and 4 since they are already set up.**

3) Start a new django project in the same directory:
```
    django-admin startproject cityevents .
```    

4) Start a new app in the project:

Start a new app in the project:
```
python manage.py startapp torontoevents
```

5) Set the python interpreter inside vscode to point to the virtual environment created with:

- To get the virtual environment path run:
```
pipenv --venv
```

- In vscode go to view -> Command Palette -> search for "Python interpreter"

- Add the path and append /bin/python at the end (eg. /Users/samirahafezi/.local/share/virtualenvs/cityevents-xqNdbNUm/bin/python)


## Django Commands

Starting the server:
```
python3 manage.py runserver
```

This starts the server on port 8000. It will give you the URL you can use to hit the landing page. Locally this should be: 
```
http://127.0.0.1:8000/
```

Get all of the django commands but in the context of the project:
```
python3 manage.py
```

## Download and Install VSCode (or an IDE of your choice)

You can get vscode from [here](https://code.visualstudio.com/). 

For VSCode install the following extensions:
- Python extension for Visual Studio Code
- Prettier Formatter for Visual Studio Code
- Pylance
- Rainbow CSV


## Download and Install Postgres db

If you're using a Macbook, [download and install Postgres](https://www.postgresql.org/download/macosx/). This will also install pgAdmin, the Postgres GUI.

It may not install `pg_config` (run `which pg_config` to confirm) and you'll need that to setup `psycopg2` (postgresql python driver)

Install Postgres with brew to get pg_config installed too (brew install postgresql)

`which pg_config` should now display: /usr/local/bin/pg_config
Then run `pip install psycopg2` to install the driver

Follow [this video](https://www.youtube.com/watch?v=unFGJhIvHU4&t=4s) to set up the right user in pgAdmin and to connect the right values in `settings.py`.

Add this to `settings.py`:
```
	DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'citydata',
        "USER": 'admin',
        "PASSWORD": 'admin',
        "HOST": 'localhost',
        "PORT": '5433',
        # "OPTIONS": {
        #     "service": "my_service",
        #     "passfile": ".my_pgpass",
        # },
	  }
	}
```

- After this the connection was set between Django dev environment and postgresql pgAdmin4
- Run python manage.py migrate to run all the migrations on the new postgresql db
- In pgadmin the tables are under citydata -> Schemas -> public -> Tables

**Some brew/Postgres commands:**
```
brew services start postgresql@15
```
```
brew services restart postgresql@15
```
```
brew info postgresql@15
```

## Debug Setup in VSCode and Chrome

- Click on the debug button on the left menu
- Select create a launch.json file
- Select Django to generate launch.json
- Update args and add port 9000:
```
	"args": [
                "runserver",
                "9000"
            ],	
```

You can also setup the django debut toolbar in Chrome for your virtual environment. To do that, follow these steps:

Setup [debug toolbar for Chrome](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) in virtual environment: 
	
- Run: 
```
python -m pip install django-debug-toolbar
```

- Open up `settings.py` and do the following steps:
```
Add  "debug_toolbar" to INSTALLED_APPS
```
```
Add "debug_toolbar.middleware.DebugToolbarMiddleware", to MIDDLEWARE
```
```
Add this anywhere:
INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]
```

- Open up `urls.py` and add the following:
```
import debug_toolbar
``` 

Add this path: 
```
path("__debug__/", include("debug_toolbar.urls")),
```
<br>

## Start the server in debug mode:

Start server on port 9000 (if you don't give port, it'll default to 8000):
```
python3 manage.py runserver 9000
```

On localhost, hit the debug URL at:
```
http://127.0.0.1:9000/
```

<br />

## GitHub Commands and how to work with the repo:
https://gist.github.com/alexpchin/102854243cd066f8b88e

- If you don't have a GitHub account, [get one](https://github.com/).
- Login to your GitHub account with the terminal ([more details here](https://cli.github.com/manual/gh_auth_login))
```
gh auth login
```

1. Clone the CityEvents repo locally:
```
gh repo clone samirahafezi/cityevents
```

In Terminal, change the current working directory to your local project.

2. Initialize the local directory as a Git repository:
```
git init
```

3. Add/modify some of the code.

4. When you're ready to commit your changes, add the files (this stages them for the first commit):
```
git add .
```

5. Commit the files that you've staged in your local repository:
```
git commit -m 'First commit'
```

6. Push your changes to the repo:
```
git push origin
```

7. You might need to connect your local respository to the remote one first. To do that, copy the remote repository URL field from your GitHub repository, in the right sidebar.

In your terminal, add the URL for the remote repository where your local repostory will be pushed:

```
git remote add origin <remote repository URL>
```

Set the new remote:
```
git remote -v
```



## Models in Django

In Django models are usually in `models.py`.

Each table is one class in the file. Eg:
```
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
```

When you create or modify a model, you'll to generate a migration file for the changes. To do that, run:
```
python manage.py makemigrations
```

To apply the changes in the migration file, run:
```
python manage.py migrate
```

To roll back a migration, run:
```
python manage.py migrate notes 0001_initial
```

This migrates it back to the 0001_initial.py version (that's the name of the migration file under migrations)

You can also do other things like squash migrations. Run this command to get more details on other useful commands under the migration umbrella:
```
python manage.py migrate --help
```

### Adding new tables to the Admin Panel

New tables do not show up in the [admin panel](http://127.0.0.1:8000/admin/) by default. You will need to explicitly add the model to the admin view.

To see the new table in the admin panel, add this to the `admin.py` file (this is an example using a Notes model with 3 fields):
```
    from django.contrib import admin
    from . import models

    class NotesAdmin(admin.ModelAdmin):
        list_display = ('field1','field2','field3',)

    admin.site.register(models.Notes, NotesAdmin)
```

Refresh the [Admin panel](http://127.0.0.1:8000/admin/) and you should be able to see the new model.

Note: To be able to login to the admin panel, you'll need to create a super user. You can do that by running this command and following the prompts:
```
python manage.py createsuperuser
```

<br />

## Adding and running cron jobs

Follow the instructions here to install and setup the [django-crontab extention](https://pypi.org/project/django-crontab/).

To add a cronjob:
```
torontoevents/cronjobs/load_locations.py:
def load_locations():
    print("HERE")
    pass

```

Add the job to the CRONJOBS block in settings.py:
```
CRONJOBS = [
    ('*/1 * * * *', 'torontoevents.cronjobs.load_locations.load_locations')
]

```
Run `python manage.py crontab add` to add it:
```
adding cronjob: (fac8222c57f1cf089c77f58b79f18d4b) -> ('*/1 * * * *', 'torontoevents.cronjobs.load_locations.load_locations')
```

Run the cronjob (the hash comes from the add command):
```
python manage.py crontab run fac8222c57f1cf089c77f58b79f18d4b
```

To remove the cron job:
```		
python manage.py crontab remove
```

To show all jobs:
```
python manage.py crontab show
```

<br />

## WIP -- Using the Django Python shell
python manage.py shell
>>> from notes.models import Notes
>>>  mynote = Notes.object.get(pk='1')
>>>  mynote.title
'First Note'
>>> mynote.text
'Testing'
>>> mynote.created
datetime.datetime(2024, 1, 14, 2, 7, 3, 332863, tzinfo=datetime.timezone.utc)
>>> mynote = Notes.objects.get(title='First Note')
>>> mynote.pk
1

>>> Notes.objects.all()
<QuerySet [<Notes: Notes object (1)>]>

>>> new_note = Notes.objects.create(title="A second note", text="Testing another note")
>>> Notes.objects.filter(title__startswith="A")
>>> Notes.objects.filter(text__icontains="Django")
>>> Notes.objects.exclude(text__icontains="Django") #excludes notes that contain the word Django
>>> Notes.objects.filter(text__icontains="Django").exclude(text__icontains="Samira")

>>> Location.objects.all().delete() #delete all the records in the table Location

To leave the shell:
>>> exit()

https://docs.djangoproject.com/en/5.0/topics/db/queries/



