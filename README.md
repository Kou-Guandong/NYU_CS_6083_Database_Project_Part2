This is a course project for CS-GY 6083 Spring 2020 semester in NYU Tandon School of Engineering.

# Environment & Skillet
- Python 3.7
- PostgreSQL


## Install dependencies
```shell
brew install postgresql # if PostgreSQL not installed 
pip install psycopg2-binary==2.8.3  # use a stable version  
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


