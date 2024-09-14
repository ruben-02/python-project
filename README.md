
# Python-Project
_A simple student management web application with CRUD operations developed in Django,MYSQL and React Js_

## Requirements
Make sure you have python and Node js installed on your system:
- [Python version 3.9.13](https://www.python.org/downloads/release/python-3913/) 
- [Node version 16.7.1](https://nodejs.org/en/download/)
- [Xampp version 8.0](https://www.apachefriends.org/download.html)


## Project Setup


- Open terminal and verify python version
  ```sh
    python --version
    ```
- Verify if node and npm are installed
  ```sh
    node --version
    npm -version
    ```
## Setup Backend
- Nvaigate to cloned project directory
  ```sh
    cd Python-Project
    ```
- Create a python virtual environment for backend
  ```sh
    python3 -m venv myvenv
    ```
- Activate the virtual environment
  ```sh
  # For winodws
    myvenv\Scripts\activate
  # For linux
    source myvenv/bin/activate
    ```
- Install python libraries
  ```sh
   cd backend
   pip install -r requirements.txt
    ```
- Start Django server
  ```sh
   python manage.py runserver
    ```
- Install Mysql
  ```sh
   pip install pymysql
    ```

- Install the CORS
  ```sh
   pip install django-cors-headers
    ```

- Install the Rest Framework
  ```sh
   pip install djangorestframework
    ```


- Install the database Url and mysqlclient
  ```sh
   pip install dj-database-url
   pip install mysqlclient
    ```
- Django backend server will start on http://localhost:8000/

## Setup Frontend
- Open a new terminal and navigate to frontend directory
  ```sh
   cd Python-project/frontend
    ```
- Install frontend libraries using npm
  ```sh
   npm install
    ```
- Start Node server
  ```sh
   npm start
    ```
- Once node is started you can access the application on http://localhost:3000/

