Wapyce
===================

**Wapyce** is a web application with objective to store results of accessibility validations of templates available on Github, to notify the developers about issues found during validation.

## Execute

To execute the Wapyce follow these instructions:

1. [Install, create and activate a virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/);
2. [Install dependencies](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#using-requirements-files);
    ```bash
    pip install -r requirements.txt
    ```
3. [Create the database schema of Wapyce](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate);
    ```bash
    python manage.py migrate
    ```
4. [Start a web server to run Wapyce](http://goodcode.io/articles/django-nginx-gunicorn/).
