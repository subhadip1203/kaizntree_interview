

#### Creating Super admin

Run  to create super admin `python manage.py createsuperuser`  <br>


#### Make Migrations and migrate

To make-migration : `python manage.py makemigrations` <br>
to actually migrate : `python manage.py migrate` <br>



### Run the server ubuntu /macbook

In case all the setup done prevously , the only do this

- Step 1: Run Database server

- Step 2: virtual env: `source virtualEnv/bin/activate`

- Step 3: Install packages : `pip install -r requirements.txt`
 
- Step 4: To create migration file: `python manage.py makemigrations`

- Step 5: To migrate to DB: `python manage.py migrate`

- Step 6: Run server : `python manage.py runserver`

<hr>



<!-- ### Second time and onwards Run the project

Step 1: Activate virtual environment `source virtualEnv/bin/activate` <br>
Step 2: run `python manage.py collectstatic` <br>


### run server 
Run teh Django Server : `python manage.py runserver`









<br><br><br><br>

# Details of the project setup



### Create development environment

Apple or linux: <br>
Step 1 :  Create virtual environment  `python3 -m venv virtualEnv`<br>
Step 2 :  Activate virtual environment `source virtualEnv/bin/activate`<br>
Step 3 :  when we stop wrorking on the project , deactivate virtual env : `deactivate`<br>

Windows virtual env (by powershell) <br>
install virtualenv : `pip install virtualenv` <br>
create virtual env: `python -m virtualenv  myenv` <br>
activate virtual env : `myenv\Scripts\activate` <br>

<br><br>

###  Install django realted packages

install , only if you did not install it before<br>
`pip install -r requirements.txt`


after installing any new package , <br>
use : `pip freeze > requirements.txt`

<br><br>

### Creating DJANGO project

Step 1 : Create Project `django-admin startproject lykas_django .`

<br><br>

### Work directory
get into the project : `cd lykas_django`

<br><br>

### Creating new app
first : create an new folder inside apps. give it name of the new app , example `app1`<br>
new app : `python manage.py startapp <app-name>  ./apps/<app-name>`<br>
example : `python manage.py startapp app1 ./apps/app1`<br>
example : `python manage.py startapp auth_app ./apps/auth_app`<br>

<br>

inside each folder , there will be file : apps.py. <br>
in side file , there will be `<appname>_config class` <br>
change name  from `<appname>` to `apps.<appname>` <br>


add paths of those apps in the main `urls.py`` files
```
path("", include("apps.home.urls")),
path("app1/", include("apps.app1.urls")),
```
<br>

Also add app names in `settings.py` file

```
"apps.home",
"apps.app1"
```



<br><br>

### new static file added 
every time if added static file run this : `python manage.py collectstatic`
<br> static files will not work in Production. <br>
<br> in development `DEBUG = True` , only then static file will work


<br><br>

### run server 
Activate virtual environment `source virtualEnv/bin/activate`<br>
run server  : `python manage.py runserver` <br>


<br><br><br> 

### Step 3 : Run local MariaDb database (using docker)


2 types of Docker environment is there:

- Option 1 : for Windows or Mac-book - Install `docker desktop` from https://www.docker.com/products/docker-desktop/

- Option 2 : Linux like Ubuntu (install native docker) 

After installtion is complete 

- Step 1: open docker-dsktop (if on windows / mac) . For ubuntu ignore thos step as docker is alys open  in background

- In the project file you will find `docker-compose.yml`, we have to run this

- Run the Database and Databse-UI by `docker-compose up -d`

- If all ok , open `http://localhost:8080/`

- PHP-My-Admin is the DB UI : to check databse details, use these credentials
  - Username: `root`
  - Password: `pass`

:warning: **The databse is only for test case**: Be very careful here!
<br>
:warning: **Usrname: root & Password : pass**: Never ( I mean never never never) use this in production

link : https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions

https://www.youtube.com/watch?v=Kc1Q_ayAeQk
-->



