# CSCI-4560-Project

This project is a Doctor Patient portal my colleagues and I have created. We use Django REST FRAMEWORK and MYSQL for our backend and React for our frontend. For set up, I am using a Windows machine, this can be done on Linux or Unix as well but the commands run in the CLI will slightly differ.

## Step 1: Create a folder for python venv

Venv is python's virtual enviroment and is used to manage package installations for project dependencies. This is so the package installations don't alter or mess up other projects you may have installed/running on your machine.

To do this, simply create a folder using the mkdir folderName command, and then executing the command: 
*python -m venv /path/to/new/virtual/environment*

**NOTE**: Any time that you would like to enter the venv for the project, simply go to the scripts folder created by the command and type the correct activate exectuion file for your system. 

Once you are in your venv, your CLI should look something like this:
![venv activation](https://github.com/Michael-Picc/CSCI-4560-Project/assets/136484545/88cc7e63-1a42-4168-8a0f-ac89253a311d)


Now create a new directory for your application using the mkdir command, I called mine mydjangoapp:
*mkdir mydjangoapp*


## Step 2: Clone the repo for requirements.txt

To clone a repo on github, go to https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository and follow the step by step guide there. If you are unsure on how to do that, simply create a requirements.txt file in your newly created application folder using the command notepad requirements.txt and copy and paste the text file into your own. Save it, and you're good to go for the next step!

## Step 3: pip install requirements

This step is an easy step but a crucial one, without it, the packages would never be isntalled. Since we have created a requirements.txt file, all we have to do to install every package needed is run the following command: *pip install -r requirements.txt* Note: if that does not work for you, run each pip install individually!

Once it runs, you should see something like this:
![pip install requirements.txt](https://github.com/Michael-Picc/CSCI-4560-Project/assets/136484545/b284f9f7-697b-4931-a628-2390efa4f2c3)


## Step 4: Initialize and run the project

This is just to make sure everything it running properly, there is much more to do before the app is ready for production.
Simply run the following commands one after another in your application folder:  
*django-admin startproject projectName
cd projectName
python manage.py runserver*

Once you run that final command, you should see something like this pop up in your command line:
![Django running in CL](https://github.com/Michael-Picc/CSCI-4560-Project/assets/136484545/fe3fd613-5e9a-4cb0-b089-2ac04b878e42)

If you were to copy and paste that link in your web browser of preference, you would see your django application is up and running in your local host!
Click Ctrl+C to close the server for now as we are going to be making multiple changes to it for our django project

## Step 5: Setup Django REST Framework
This can all be done in Command line, but for simplicities sake, I will be using VS Code for any changes to the application itself which many of the following steps will be doing.

Go to settings.py and at the bottom of INSTALLED_APPS add: **'rest_framework',**

## Step 6: Create Django app to logically seperate features

This step makes it easy to transfer 'apps' into other projects.

simply run the following command:
*python manage.py startapp appName*

## Step 7: Connect Django to your mysql database
If you would prefer skipping this step, it is completely optional but does add additional security to your application.
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

## Step 8: Build your Models

In your models.py file you have the liberty to create any objects, classes, or tables that you desire. Here is what mine looks like for this project:
[models.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/myapp/models.py)

Your models are your tables and their fields in mysql, it is just setting them up for Django to use.

## Step 9: Create your Serializers
Again, this is an optional step but will create a dashboard for your database which i highly recommend having for ease of access.
While handling GET requests, we need a way of transforming complex model instances, into JSON, so we can send the data back via an HTTP response. Likewise, if a user sends data to our API via a POST or PUT request, we need a way to validate the data for integrity and security purposes before allowing that user request to add data to our database. We can achieve both of these tasks with serializers, which is a concept provided by Django Rest Framework.

In the app you have created, create a file called serializers.py and fill it with the necessary information for your app.

Here is what our serializers.py looks like:

[serializers.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/myapp/serializers.py)

## Step 10: Create your Views
Django Views are the backbone for CRUD applications built in it. This is how we will handle our GET,POST,PUT, and DELETE.

In your app, create the views.py and fill it with what is necessarry for your app.

This is our views.py:
[views.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/myapp/views.py)

## Step 11: Clean up and add to our Setting.py
Even though we have added multiple lines of code to our settings.py, there are a few more we need to add. We are going to change the user model Django uses by default to the one we created in models by adding this line after authorized hosts, *AUTH_USER_MODEL = 'myapp.Profile'*, and then we are going to add a few lines of code at the bottom fo the settings.py to point django towards our static files (HTML, CSS, PNG). It should look something like this when we are done.

[settings.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/settings.py)

## Step 12: Fix up your URLS and add your html files
These will be the names of your browser locations of your API.

Create your urls.py in your app and name them and fill them with the necessary information

This is our urls.py in the app:
[myapp/urls.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/myapp/urls.py)

after this is done, go to your django project urls.py that was created when you created the Django project and at the bottom of the file,
add your newly created app to the urlpatterns. It should look something like this:

[pd_portal/urls.py](https://github.com/Michael-Picc/CSCI-4560-Project/blob/main/mydjangoapp/pd_portal/ur.py)

Once that it done we now need to create a templates folder in our app and inside of that create a folder named the same name as the app you created in previous steps. In this nested folder, we are going to copy and paste all of our html and css files and static images. The {} throughout the html are python code embedded into the html to provide functionality and you can do the same to yours. Whenever you want to use python in your html in Django, you must start your html file with {% block content %} followed by {% load static %}. The first is to tell Django there is python code in this html file and the 2nd is so Django knows this html file is static and has css attached to it. Lastly, whenever you have an href link, always format the link like so:<link href="{% static 'homepage.css'%}" rel="stylesheet"> this is for Django to know this references a static css file within Django. The last step of this part is to go back to your CLI and run *python manage.py collectstatic* to make sure Django correctly identifies your static css and html.

## Step 13: Migrate

To finalize these changes in your app, quit the server if you haven't already using ctrl+c, and then the following commands:
*python manage.py showmigrations* This is an optional command, shows you what migrations will be executed
*python manage.py migrate*
**NOTE:** If you are running into errors with the showmigrations command and the error has to do with an unknown database, that means you have not created the database of said name

Running those two commands should yield the following results:

![showmigrations](https://github.com/Michael-Picc/CSCI-4560-Project/assets/136484545/303afcbd-57ca-4f22-a031-98352673ff81)
![migrate](https://github.com/Michael-Picc/CSCI-4560-Project/assets/136484545/1c8ff51c-c380-4036-addb-db9ff29e3900)


## Step 13: Congrats, You have finished your rest api!
Now you get to the fun part and get to play around and insert data into your database through an api :)! Go back to your CLI and run *python manage.py runserver* in the directory containing your manage.py file and go buck wild! You can go to any of the url locations you created and create,read,update, or delete any items in your tables. You also have the custom urls we created along the way for added functionality.






