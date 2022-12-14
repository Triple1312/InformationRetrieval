# InformationRetrieval

## Scope

Google scholar is a service that makes it easy to browse hundreds of available papers on the internet, but some papers can be quite large. 
We want to extend this searching process down to the paper level itself. 
Our project will search in the paper and produce and abstract containing all the important keywords. 
This way, the user does not have to read the entire paper only to find one (possibly) useful resource. 
We can extend the project by adding a feature where the user can specify which words they think are important. 

## Resources

### Data sources

It should be possible to use every paper on google scholar. 
But for testing purposes, we are going to use the papers which already have an abstract. 
That way, we can compare the results (which is an abstract) of our system to the abstract given in the paper.

### Tools

The first tool is the TF.IDF scoring method. This will be used when our systems searches through the paper. 
Then we will use some neural models to construct the abstract of the paper.

## Literature

1.	Modern Information Retrieval: the concepts and technology behind search
By Richardo baeza-yates, Berthier Rihbeiro-Neto
2.	Introduction to Information Retrieval 
By Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze
3.	The course slides

## Evaluation

Some papers already have an abstract. Our project won’t be very useful on these papers, but these papers can be handy for evaluating our project. 
We let our system run on the contents of the paper (without the abstract) and compare the results of our system to the given abstract from the paper. 
Based on this comparation, we can create a scoring system that can improve our system.

## Installation
### Backend
The backend is written in python. To install the required packages, run the following command in the backend folder:
```
pip install -r requirements.txt
```
The backend itself uses the django framework. To run the backend, run the following command in the backend folder:
```
python manage.py runserver
```

### Database
The database system used is postgres 14. First, create the database and a new user with the following commands:
```sql
CREATE USER ir_user WITH SUPERUSER PASSWORD 'IR_PW';
CREATE DATABASE ir_db OWNER ir_user;
```
Next, configure the pg_hba.conf file to allow the user to connect to the database. The file can be found in the data 
folder of the postgres installation. Add the following line to the file:
```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   ir_db           ir_user                                 trust

```


