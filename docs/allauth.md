# TUTORIAL ON ALLAUTH

## SETUP 
- install alluth using command `pip install django-allauth`
- add `allauth` and `allauth.account` to `INSTALLED_APPS` array in `setting.py`
- add `"allauth.account.middleware.AccountMiddleware"` to `MIDDLEWARE` array
- include allauth urls in root url conf
- run migrate command
- run the server
