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
3. [Install PostgreSQL](https://wiki.postgresql.org/wiki/Detailed_installation_guides);
4. Configure enviroment variables;
    ```bash
    # Production environment
    export DATABASE_NAME=wapyce
    export DATABASE_USER=postgres
    export DATABASE_PASSWORD=postgres
    export DATABASE_HOST=localhost
    export DATABASE_PORT=5432

    # Development environment
    export DJANGO_SETTINGS_MODULE=config.settings.local
    export DATABASE_LOCAL_NAME=wapyce_local
    export DATABASE_LOCAL_USER=postgres
    export DATABASE_LOCAL_PASSWORD=postgres
    export DATABASE_LOCAL_HOST=localhost
    export DATABASE_LOCAL_PORT=5432

    # Tests environment
    export DJANGO_SETTINGS_MODULE=config.settings.test
    export DATABASE_TEST_NAME=wapyce_test
    export DATABASE_TEST_USER=postgres
    export DATABASE_TEST_PASSWORD=postgres
    export DATABASE_TEST_HOST=localhost
    export DATABASE_TEST_PORT=5432
    ```
5. [Create the database schema of Wapyce](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate);
    ```bash
    python manage.py migrate
    ```
6. [Start a web server to run Wapyce](http://goodcode.io/articles/django-nginx-gunicorn/).

## Contributing

If you want contribute with Wapyce, read [contributing guidelines](CONTRIBUTING.md).

## Donate
  
If you'd like to monetarily support Wapyce development, you can:

* Donate Bitcoin to **36QNXpPzUDLdt611E2t3wdr9zBhWePBJga** wallet address;
* Donate Ethereum to **0xd7446224eb2da4f41f5f68f82be01e1f5fa1940e** wallet address;
* Donate Litecoin to **LVgF8LE8n6jFrKKfYZoyh9eckx2oBxcaGP** wallet address;
* Donate Waves to **3P7Hapj4Kvbn1k9GN2reb8aUsyDjNPy6pbS** wallet address;
* Donate Zcash to **t1dpafSCveZqa4mwk5Lrf55uKzPLVWCQLf6** wallet address;
* Donate Bitcoin Cash to **qp5sz7q3yxhrca7cvq54wktrk8392pgd9ucetl3w6n** wallet address.
