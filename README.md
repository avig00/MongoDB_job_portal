# DS5760 NoSQL for Modern Data Science Applications:
# Mini Project 2 – CareerHub: Building a Mini Job Portal with MongoDB and Flask

## About
CareerHub is a MongoDB based career portal database. It allows users to retrieve and modify job listings based on specific criteria.

## Requirements
CareerHub requires the following:
* Docker
* Python
* MongoDB
* PyMongo
* Flask

## Installation
The required tools can be installed via pip. As an example, the code block below shows how to install PyMongo.
```
pip install pymongo
```

## Setting up
1. Once all the requirements have been installed, the CSV files can be converted to json by running the csv_to_json.py file:
`pyton csv_to_json.py`

2. The MongoDB container is defined in the docker-compose.yml file, and can be started using the following command:
   `docker-compose up`

3. Access the mongo shell (this is required to import data from the json files)
   `docker compose-exec mongodb sh`

6. Once in the shell, data can be imported into the database using these lines:

   - `mongoimport --db careerhub --collection listings --file /ds5760/mongo/data/listings.json --jsonArray`
   - `mongoimport --db careerhub --collection company_and_industry_info  --file /ds5760/mongo/data/company_and_industry_info.json --jsonArray`

7. To verify that the imports are successful, we can run the following code:
`docker-compose exec mongodb mongosh`

This allows us to access the database and see what collections it contains.

8. Finally, run the flask app to start dynamically interacting with the CareerHub database.
   `python run-app.py`

## End Point Information

1. `http://127.0.0.1:5000/`

   - METHOD = GET
   - This end point is the root URL of the Flask App, which simply displays a welcome message to users.


2. `http://127.0.0.1:5000/create/jobPost`

   - METHOD = POST
   - This end point is used to create a new job post
   - Parameters:
        - title: Title of the job
        - description: Description of the job duties
        - industry: Industry that the job belongs to
        - average_salary: Average salary for the job
        - location: Location of the job
   - Example: http://127.0.0.1:5000/create/jobPost?title=data scientist&description=coder&industry=technology&average_salary=80000&location=boston


3. `http://127.0.0.1:5000/search_by_job_id/<job_id>`

   - METHOD = GET
   - This end point is used to retrieve information about a job using the job ID.
   - Parameters:
     - job_id: ID of the job that the user wants to search for. 
   - Example : http://127.0.0.1:5000/search_by_job_id/27

4. `http://127.0.0.1:5000/update_by_job_title`

   - METHOD = POST
   - This end point is used to update job posts by the job title.
   - Parameters:
     - title: Tite of the job.
     - location: Location of the job.
     - description: Description of job duties.
     - average_salary: Salary offered for the job.
   - Example : http://127.0.0.1:5000/update_by_job_title?title=Machine Learning Engineer&description=Looking for someone who canhelp manage the data/preprocessing and can work with the tech team.&average_salary=95000&location=Nashville&industry=Tech

5. `http://127.0.0.1:5000/delete_by_job_title`

   - METHOD = DELETE
   - This end point is used to delete job posts by the job title.
   - Parameters:
     - title: Name of the job.
     - confirmation: Should be "Yes" if the user wants to proceed with deleting job posts.
   - Example : http://127.0.0.1:5000/delete_by_job_title?title=Investment Data Analyst&confirmation=Yes

6. `http://127.0.0.1:5000/query_jobs_by_salary`

   - METHOD = GET
   - This end point is used to view all the job posts that have an average salary within a specified range.
   - Parameters:
     - minimum: The lower bound of the salary range. 
     - maximum: The upper bound of the salary range. 
   - Example : http://127.0.0.1:5000/query_jobs_by_salary?minimum=45000&maximum=50000

7. `http://127.0.0.1:5000/query_jobs_by_level`

   - METHOD = GET
   - This end point is used to get all job posts based on the required career level.
   - Parameters:
     - experience_level: Career level -
        - Entry - years of experience < 3.
        - Mid - years of experience between 3 and 6 (both inclusive).
        - Senior - years of experience > 6.
   - Example : http://127.0.0.1:5000/query_jobs_by_level?experience_level=Senior

8. `http://127.0.0.1:5000/top_companies_by_industry/<industry_name>`

   - METHOD = GET
   - This end point is used to get the names of companies in a given industry, with the companies sorted in descending order of total number of job posts.
   - Parameters:
     - industry_name: The industry for which the user wants to retrieve the top companies. 
   - Example : http://127.0.0.1:5000/top_companies_by_industry/Finance
