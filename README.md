
# Development

## Install dependencies
```shell
brew install postgresql
# pip install psycopg2 # with bugs incurred
pip install psycopg2-binary==2.8.3
```

## start application (only for dev)
```
python manage.py startapp insurance
```

## Migrate database
```sh
python manage.py migrate
```



