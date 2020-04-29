This is a course project for CS-GY 6083 Spring 2020 semester in NYU Tandon School of Engineering.

# Environment & Toolset
- Python 3.7
- PostgreSQL


## Install dependencies
```shell script
brew install postgresql # if PostgreSQL not installed 
pip install psycopg2-binary==2.8.3  # use a stable version  
```

## Migrate database when model changed
```shell script
python manage.py makemigrations insurance
python manage.py migrate
```

## Reset sequence for data tables
```shell script
python manage.py sqlsequencereset insurance| python manage.py dbshell
```

# Development

## Back-End
```shell script
python manage.py runserver
```

# Assumptions and Simplifications
- A customer can be enrolled in either home insurance, auto insurance, or both.
- An insurance policy can only have 1 customer, but each customer can have more than one insurance policies.
- An insurance policy can involve home, automobile, possibly both home and automobile, or even other types of property in the future. (To keep the highest flexibility and extensibility)

# Extra Features Developed

## Indexing
Index types supported by PostgreSQL: B-tree, Hash, GiST, SP-GiST and GIN.

## REST API
