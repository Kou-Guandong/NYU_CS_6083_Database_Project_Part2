
# Pre-Development

## Install dependencies
```shell
brew install postgresql
pip install psycopg2-binary==2.8.3
```

## Migrate database when model changed
```sh
python manage.py makemigrations insurance
python manage.py migrate
```

# Development

## Back-End
```shell
python manage.py runserver
```


