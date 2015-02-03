

# Tutorial
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

## Left off at
https://docs.djangoproject.com/en/1.7/intro/tutorial03/

# Install
- `$ pip install django==1.7.4`
  - or whatever the latest version is; see https://www.djangoproject.com/download/
- `$ pip install pytz`
  - Python timezone module
  - Django doesn't technically require this, because Django likes the "we can run with no 
    prerequisites" thing.  But having this installed appears to be A Good Thing.

# Scripts

## Admin script
- django-admin.py
  - django-admin.py startproject mysite
    - Project names cannot conflict with Python builtins or Django components.  So no 
      "python" or "test" etc for project names.
  - Django has both apps and projects.  The distinction is that an app is meant to do one 
    thing (a poll, an admin section, a blog, whatever).  A Project can include multiple 
    apps.
  - django-admin.py creates projects.  The manage.py inside one of those projects creates 
    apps.

## Project scripts
The following paths assume you used 'mysite' as the site name.

- mysite/mysite/settings.py
  - Edit this.  No part of the tut has mentioned running it; I assume it just gets pulled 
    in when the app runs.
  - Timezone, database setup, etc.
    - Yes, `mysite/mysite/`.
  - Contains a list of other Django applications that will be included in this one 
    (`INSTALLED_APPS`).  To initialize those apps, you'll need to use manage.py
- `mysite/manage.py`
  - Gets created automatically when you use django-admin.py to create a new project.
  - `$ python manage.py migrate`
    - Initializes the apps listed in settings.py, so you may want to edit that first 
      before running this.
    - Only runs migrations that haven't been run yet.
  - `$ python manage.py runserver`
    - start the development server
    - Defaults to port 8000.  If you want, change with $ python manage.py runserver 8080 
      (or whatever)
    - Autodetects and reloads itself on changes in existing files.
      - Does _not_ detect new files; for that you need to do a manual restart.
      - If you save a syntax error while this auto-reloading is running, it'll explode.  
        Just fix your error and restart it.
    - http://localhost:8000/
    - http://localhost:8000/admin
      - provided you left the admin contribution in INSTALLED_APPS in settings.py
      - This is pretty seksi.  Overall it's doing basic stuff, but it's doing it well and 
        thoroughly.
  - `$ python manage.py startapp <APPNAME>`
    - Creates an app under your project
    - After your app has been set up, add its name to your site's settings.py under 
      `INSTALLED_APPS`.
  - `$ python manage.py makemigrations <APPNAME>`
    - Uses <APPNAME>'s models to generate migration scripts
  - `$ python manage.py sqlmigrate <APPNAME> <MIGRATION_NUMBER>`
    - Displays the SQL for a given app's given migration.
  - `$ python manage.py check`
    - Checks for problems in your project without making any changes.
  - `$ python manage.py shell`
    - Starts a python shell, much like simply running `$ python` would do.  But doing it 
      via manage.py sets some paths so the shell knows how to find your app components.
    - https://docs.djangoproject.com/en/1.7/intro/tutorial01/
      - Search for "Once you’re in the shell, explore the" for examples of how to browse 
        models using the shell.
  - `$ python manage.py createsuperuser`
    - Starts an interactive session in which you enter login creds for your superuser, who 
      will be able to access the admin site.

## App scripts
- `<APPNAME>/models.py`
  - See the Models section for details.
- `<APPNAME>/admin.py`
  - Edit this to tell the admin section app that this app should have an admin interface.
  - See polls/admin.py for eg

# Models
After creating an app, you'll have <APPNAME>/models.py.  Add models to this as classes.  
See polls/models.py as eg.

After setting up your model, remember to run "manage.py makemigrations <APPNAME>."  To see 
the SQL in any of the individual migrations:
    $ python manage.py sqlmigrate polls 0001

When you're happy with that, go ahead and run your new models' migrations:
    $ python manage.py migrate

Any time you need to make changes to your models, re-run manage.py with first 
`makemigrations`, and then `migrate`.

# Templates
- No templates directory gets created as part of the initial setup.  If you want custom 
  templates, create a directory under your project directory) and add its name to 
  `mysite/settings.py`.  I'll assume you're naming your directory "templates".
  - `TEMPLATE_DIRS = [ os.path.join(BASE_DIR, 'templates')]`

- To modify the look of the admin section:
  - Create templates/admin/
  - Copy the default template from the contributed admin app into your new admin/ 
    directory.
    - I found the admin app's templates here:
      ~/work/python/virtualenvs/Django/lib/python3.4/site-packages/django/contrib/admin/templates/admin/

