# Mifugo

## Description

I was inspired to build this application since my father wanted to track the animals in the farm and this way I can build it to the cutom needs in Tanzania.
I am also thinking of adding multiple language support Swahili and English so that people more comfortable with Swahili can use it aswell.

## Stack

This is Django Rest project with React in its own “frontend” Django app where I load a single HTML template and let React manage the frontend.

Keeping React closer to Django makes easier to reason about authentication and other stuff.

- The project can exploit the Django's built in authentication for registering and logging in users.
- The app can exploit Session authentication and not worry too much about tokens and JWT.

## Development

Currently using sqlite, will definetly be switching db soon. For now its okay.

You can use my sample archive data to start immidiately playing aroud with the stuff.
These are real animals tht I personally went and tagged and also identified parents and children by observing them nursing.

### Virtual Evironment

- Clone this repo
- Create a vitual environment `virtualenv venv`
- Activate the virtual environment `source venv/bin/activate`
- Install dependencies using `npm` and `pip`
- Migrate the database `python manage.py migrate`

If you choose to have my sample data:

- Create a super user `python manage.py createsuperuser`

```bash
# Let the super user be name karim since my script looks for karim and respect my data haha 😂
Username (leave blank to use 'karim'): 
Email address:
Password:
Password (again):
```

- Add the archive data as sample if you choose to `python manage.py restore_from_archive`
- Run the app `npm run dev` and then `python manage.py runserver`

## LICENSE

[MIT LICENSE](LICENSE)