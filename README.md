# Blue Drive Test Project

## Local Development without Docker

### Install

```bash
python3 -m venv env && source env/bin/activate                # activate venv
pip install -r requirements.txt                               # install py requirements
./manage.py migrate                                           # run migrations
```

### Run dev server

This will run server on [http://localhost:8000](http://localhost:8000)

```bash
./manage.py runserver
```

### Create superuser

If you want, you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```
