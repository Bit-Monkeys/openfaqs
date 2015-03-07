# openfaqs

An Open Source FAQ Board 

# Deployment  

We are running our development environment on Ubuntu 14.04 LTS. 

## Installation Instructions 

### Shared Development Database 

We have a public shared dev database with "real" data in it, if you wish to get access to this DB please let @levlaz know. This makes it a bit easier to see the app in action and work from a common data set. 

1. Install git, mysql-server, pip

    `apt-get install git mysql-server python-pip python-dev libmysqlclient-dev`

2. Create openfaqs_admin user, feel free to change the password but be sure to update it in /openfaqs/openfaqs/settings.py if you do. 

    ```
    mysql -u root -p 
    create database openfaqs; 
    grant all on openfaqs.* to 'openfaqs' identified by 'openfaqs';
    ```
    
3. Clone this repo 

	`git clone https://github.com/Bit-Monkeys/openfaqs.git`
	
4. Go into the openfaqs directiory and install Flask and dependencies 

	```
	cd openfaqs
	pip install -r config/requirements.txt
	```

6. Start the OpenFaqs App 
    
    ```
    python app.py 
    ```

7. Access it on http://localhost:5000 


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

