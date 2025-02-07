## Django Email
- Setting up an email environment in django using gmail


### STEPS 
- create evironmental variables `.env` file
- Write the following variables into it
    ```sh
    EMAIL_HOST="smtp.gmail.com" # host
    EMAIL_PORT=587 # email port
    EMAIL_HOST_USER="hungrypy@gmail.com" ## your email account name
    EMAIL_HOST_PASSWORD="byeu ioni opaen ak" # your password
    EMAIL_USE_TLS=True # for security set TLS/SSL to True; if you want to use either one
    EMAIL_USE_SSL=False 
    ```
- Go to My Google Account(https://myaccount.google.com).
- Search for "App Password"
- Copy the App Password for your Django project's environment variables. Such as `.env` or in your production systems environment variables (over time you should upgrade to a domain you own with a production-ready transactional email service)
- Add the following line to `settings.py` 
    ```py
    ADMIN_USER_NAME=config("ADMIN_USER_NAME", default="Admin user")
    ADMIN_USER_EMAIL=config("ADMIN_USER_EMAIL", default=None)

    MANAGERS=[]
    ADMINS=[]
    if all([ADMIN_USER_NAME, ADMIN_USER_EMAIL]):
        ADMINS +=[
            (f'{ADMIN_USER_NAME}', f'{ADMIN_USER_EMAIL}')
        ]
        MANAGERS=ADMINS
    ```
- Add `ADMIN_USER_EMAIL=` to the `.env` file
- Run `python manage.py sendtestemail --admins`