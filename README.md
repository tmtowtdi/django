

# Tutorial
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Scripts
- django-admin.py
  - django-admin.py startproject mysite
    - Project names cannot conflict with Python builtins or Django components.  So no 
      "python" or "test" etc for project names.

## Project scripts
The following paths assume you used 'mysite' as the site name.

- mysite/manage.py
  - Gets created automatically when you use django-admin.py to create a new project.
- mysite/mysite/settings.py
  - Timezone, database setup, etc.
  - Yes, `mysite/mysite/`.


