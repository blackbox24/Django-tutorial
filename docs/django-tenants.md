## Django Tenants Package

### INSTALLATIONS
- [x] install package `pip install django-tenants psycopg2-binary`

### BASIC CONFI
- [x] add `django_tenants.middleware.main.TenantMainMiddle` to `MIDDLEWARE`
- [x] add `django_tenants.postgresql_backend` as `engine` in `DATABASE` root settings.py
- [x] add `django_tenants.router.TenantSyncRouter` as an element of `DATABASE_ROUTERS` tuple
- [x] create `client` app `py manage.py startapp client`
- [x] create `SHARED_APPS` to contain all shared apps (ommon to every tenant) and pass list of shared apps
    ```py
    # example
    SHARED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    
- [x] create `TENANT_APPS` app which will be responsible for each tenant
- [x] combine `TENANT_APPS` AND `SHARED_APPS` into `INSTALLED_APPS`
- [x] add package name `django_tenants` to `SHARED_APPS` in `setting.py`
- [x] Make sure you have `django.template.context_processors.request` listed under the `context_processors` option of `TEMPLATES` otherwise the tenant will not be available on `request`.
- [x] inside your client app, create a class called Client inhereiting from TenantMixin and pass its attribute
- [x] inside your client app, create a class called Domain inhereiting from DomainMixin and pass its attribute
- [x] run `python manage.py migrate_schema` to make migrations to postgres schema
- [x] run `python manage.py create_tenant` followin prompt to create a tenant
- [x] run the server and access your main tenant using the primary tenant 
    Note: In your prompt you will be ask if you want the tenant to be the primary one. If your choose yes then use that domain.

    ```sh
    http://demo2.localhost:8000/login

    ```