# Side Effects Management


### Getting Started
1. Install Flask
```
pip install flask
```
2. Install the MySQL Connector/Python 
```
pip install mysql-connector-python
```
3. Install MySQL workbench from https://dev.mysql.com/downloads/workbench/
4. Create a username and password in MySQL workbench to access the database (https://dev.mysql.com/doc/workbench/en/wb-mysql-connections-navigator-management-users-and-privileges.html). 
5. Navigate to the app/ directory on your local setup. Check that there is a file called 'app.py'
6. Inside 'app.py', update the username and password inside the 'config' object near the top of the file.
7. Fire up a flask server.
```
flask run
```
8. Download Postman from https://www.getpostman.com/downloads/
9. Now you should be able to test API requests via Postman and see any associated changes in MySQL workbench.

## Backend NLP 

The backend NLP folder contains the code that parse the user string. 

1) Read the user string passed as parameter via the API call 
2) Pre-process the query string and find the feature vector 
3) Match similarity with that of the DB content, find the best match 
4) Respond back with the comments corresponding to the best match 

