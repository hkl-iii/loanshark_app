# Loanshark

## Project requirements

* [Python >= 3.0](https://docs.python.org/3)
* [Django >= 3.0](https://docs.djangoproject.com/en/3.0/)
* [Django RestFramework](https://www.django-rest-framework.org/)
* [Bootstrap documentation - more features](https://getbootstrap.com/docs/4.1/getting-started/introduction)
* [React.js](https://reactjs.org/)




## Setup 
* On project initialization, clone the repository using

git clone https://github.com/hkl-iii/loanshark_app.git
Note: This needs to be done only once

## Setup the Django Backend by installing the requirements 

```
cd loanshark_app\backend\loanshark
```

```
pip install -r requirements.txt
```
## Apply the migrations to DB
```
python manage.py migrate
```
## Run the project with the command 
```
python manage.py runserver
```
 

## Setup the React Frontend 
```
cd loanshark_app\frontend\loanshark
```
```
npm install 
```
## Run the project with the command 
```
npm run start 
```