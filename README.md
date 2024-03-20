# CSCI-4560-Project

This project is a Doctor Patient portal my colleagues and I have created. We use Django REST FRAMEWORK and MYSQL for our backend and React for our frontend. For set up, I am using a Windows machine, this can be done on Linux or Unix as well but the commands run in the CLI will slightly differ.

## Step 1: Create a folder for python venv

Venv is python's virtual enviroment and is used to manage package installations for project dependencies. This is so the package installations don't alter or mess up other projects you may have installed/running on your machine.

To do this, simply create a folder using the mkdir folderName command, and then executing the command: 
*python -m venv /path/to/new/virtual/environment*

**NOTE**: Any time that you would like to enter the venv for the project, simply go to the scripts folder created by the command and type the correct activate exectuion file for your system. 

Once you are in your venv, your CLI should look something like this:
INSERT IMAGE

Now create a new directory for your application using the mkdir command, I called mine mydjangoapp:
*mkdir mydjangoapp*


## Step 2: Clone the repo for requirements.txt

To clone a repo on github, go to https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository and follow the step by step guide there. If you are unsure on how to do that, simply create a requirements.txt file in your newly created application folder using the command notepad requirements.txt and copy and paste the text file into your own. Save it, and you're good to go for the next step!

## Step 3: pip install requirements

This step is an easy step but a crucial one, without it, the packages would never be isntalled. Since we have created a requirements.txt file, all we have to do to install every package needed is run the following command: *pip install -r requirements.txt*

Once it runs, you should see something like this:
INSERT IMAGE

## Step 4: Initialize and run the project

This is just to make sure everything it running properly, there is much more to do before the app is ready for production.
Simply run the following commands one after another in your application folder:  
*django-admin startproject projectName
cd projectName
python manage.py runserver*

Once you run that final command, you should see something like this pop up in your command line:
INSERT IMAGE

If you were to copy and paste that link in your web browser of preference, you would see your django application is up and running in your local host!

## Step 5: Setup Django REST Framework

This can all be done in Command line, but for simplicities sake, I will be using VS Code for any changes to the application itself which many of the following steps will be doing.

Go to settings.py and at the bottom of INSTALLED_APPS add: **'rest_framework',**

## Step 6: Create Django app to logically seperate features

This step makes it easy to transfer 'apps' into other projects.

simply run the following command:
*python manage.py startapp appName*

## Step 7: Connect Django to your mysql database

First verify that your mysql database you are to connect to is up and running, and create one with a name of your choosing. 
This can be done using Mysql workbench or the CLI it is up to. 
Once you are done with that, go back to the settings.py of your django project and update the DATABASES variable to use mysql instead of sqlite. 
It should look like this:
*DATABASES = {
  'default': {
    # MySQL engine. Powered by the mysqlclient module.
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'example',
    'USER': 'root',
    'PASSWORD': 'xxx',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}*

## Step 8: Migrate

To finalize these changes in your app, quit the server if you haven't already using ctrl+c, and then the following commands:
*python manage.py showmigrations* This is an optional command, shows you what migrations will be executed
*python manage.py migrate*
**NOTE:** If you are running into errors with the showmigrations command and the error has to do with an unknown database, that means you have not created the database of said name

Running those two commands should yield the following results:
INSERT IMAGE
INSERT IMAGE

## Step 9: Build your Models

In your models.py file you have the liberty to create any objects, classes, or tables that you desire. Here is what mine looks like for this project:
INSERT IMAGE

## Step 10: Create your Serializers

## Step 11: Create your Views

## Step 12: Fix up your URLS

## Step 13: Congrats, You have finished your rest api!
Now you get to the fun part and get to play around and insert data into your database through an api :)!






