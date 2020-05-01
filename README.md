This is a course project for CS-GY 6083 Spring 2020 semester in NYU Tandon School of Engineering.

# Environment & Toolset
- Python 3.7
- PostgreSQL

## Install dependencies
```shell script
brew install postgresql # if PostgreSQL not installed 
pip install psycopg2-binary==2.8.3  # use a stable version  
```

# Development

## Back-End
```shell script
python manage.py runserver
```

## Migrate database 
### when models changed
```shell script
python manage.py makemigrations insurance
python manage.py migrate
```
### Reset sequence for data tables
```shell script
python manage.py sqlsequencereset insurance | python manage.py dbshell
```

# Assumptions and Simplifications of Project Scenario

## Business work flow
- This website is developed by WDS company to attract customers to enroll in home and auto insurance
- A customer can register and log into account, and view general data at the client website
- Only WDS staff can login to the administration system and perform operations
- Before an insurance policy is issued, WDS staff need to evaluate the risk of homes and vehicles
- There will be negotiations between the customer and WDS staff of the following aspects
    - insurance amount and time span
    - invoice amount and period
    - payment method and period
- Once a deal is made, WDS staff and the customer will confirm and sign a contract with insurance policy;
Later on, invoice(s) will be mailed to customer, and the customer needs to make payment(s)

## Relations of Entities
- A customer can be engaged in one or more policies.
- Each insurance policy may cover 0, one or many homes, and 0, one or many vehicles.
    - This is to maintain the highest flexibility and extensibility, 
    sometimes the business team can make capricious decisions,
    sometimes the policy needs to adjust to the market, e.g. make discount for multiple properties insured 

# Extra Features Developed

## Security
- Anti XSS via CSRF tokens
- Anti SQL injection via ORM connected to database

## Indexing
Index types supported by PostgreSQL: B-tree, Hash, GiST, SP-GiST and GIN.

## REST API
Achieved by using [`django-rest-framework`](https://www.django-rest-framework.org/)


# Selection of Database and Frameworks
## Pros and Cons of PostgreSQL

### Advantages of PostgreSQL
- Efficiency in handling transaction concurrency with sophisticated locking mechanism
- High SQL compliance, with 160/179 features required for full core SQL:2011
- Highly fault-tolerant given to its write-ahead logging
- Object-Relational database, supports JSON, image, video, audio and graphical data
- Low maintenance cost; Open source license; highly robust and reliable; etc.

### Disadvantages of PostgreSQL
- Lower speed for read-heavy operations than MySQL

## Django
features: Model-View-Template (MVT)
- Efficient development
    - auto-generated database tables
    - auto-generated admin UI
- Security
    - validation of form fields
    - user session, authentication management 
