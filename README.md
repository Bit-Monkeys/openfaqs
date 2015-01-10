# openfaqs

An Open Source FAQ Board 

![travis](https://travis-ci.org/levlaz/openfaqs.svg?branch=master)

# Deployment  

We are running our development environment on Ubuntu 14.04 LTS. 

## Software Versions 

Software | Version 
---------|---------
Ubuntu   | 14.04 LTS 
MySQL-Server | mysql  Ver 14.14 Distrib 5.5.40 
Python      | 2.7.6  
Django      | 1.7.2 
MySQL-python | 1.2.5

## Installation Instructions 

1. Install git, mysql-server, pip

    `apt-get install git mysql-server python-pip python-dev libmysqlpython-dev`

2. Install Python Dependencies  

    `pip install django MySQL-python` 

3. Create openfaqs_admin user, feel free to change the password but be sure to update it in /openfaqs/openfaqs/settings.py if you do. 

    ```
    mysql -u root -p 
    create database openfaqs; 
    grant all on openfaqs.* to 'openfaqs_admin' identified by 'faterror53';
    ```
    
4. Sync the DB 

    `python manage.py migrate` 

5. Create a superuser (to access /admin) 

    `python manage.py createsuperuser` 

6. Start the OpenFaqs App 
    
    ```
    python manage.py runserver (if testing localy) 

    python manage.py runserver 0.0.0.0:8000 (if testing remotely) 
    ```

7. Access it on http://localhost:8000 


# Development  

1. Fork This Repo 

2. Clone your Fork Locally 

	`git clone git@github.com:$username/openfaqs.git`

3. Set Up Remote Repo 

	`git remote add upstream git@github.com:Bit-Monkeys/openfaqs.git`

4. Sync your Fork  
	
	``` 
	git fetch upstream 
	git checkout master 
	git merge upstream/master 
	git push -u origin master
	```

5. Hack away in your local repo, remember to always sync with the master before making any major changes to avoid git hell. :) 
6. Push changes to your local repo, test, and submit a merge request. 

