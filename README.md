

# Tutorial
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Scripts
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
  - Timezone, database setup, etc.
    - Yes, `mysite/mysite/`.
  - Contains a list of other Django applications that will be included in this one 
    (`INSTALLED_APPS`).  To initialize those apps, you'll need to use manage.py
- mysite/manage.py
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

## Models
After creating an app, you'll have <APPNAME>/models.py.  Add models to this as classes.  
See polls/models.py as eg.

After setting up your model, remember to run "manage.py makemigrations <APPNAME>."  To see 
the SQL in any of the individual migrations:
    $ python manage.py sqlmigrate polls 0001

When you're happy with that, go ahead and run your new models' migrations:
    $ python manage.py migrate

Any time you need to make changes to your models, re-run manage.py with first 
`makemigrations`, and then `migrate`.



