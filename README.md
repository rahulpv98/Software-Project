# IOT Wiki

This is a django based web application. One need to install python, django and other dependencies to run this project. It's recommended to create a virtual environment and start contributing. 
### Featuers
1. As of now only admin can add the blogs and rest can see.

### Installation Instructions
1. Install Python3 and pip
2. Install `virtualenv` and add it to your terminal path.
3. Clone the repository and create the virtual environment
    ```
      $ git clone https://github.com/rahulpv98/iot_wiki.git
      $ cd blog-aggregator
      $ virtualenv -p python3 .
      $ source bin/activate
    ```
4. Install the dependencies from `requirements.txt`
    ```
      $ pip install -r requirements.txt
    ```
### Running the Application
1. Activate the virtual environment `source bin/activate` and can be decativated with `deactivate`
2. Set up the database and run the following commands whenever models are changed
    ```
      python manage.py migrate
      python manage.py makemigrations
    ````
3. Create super user. 
    ```
      python manage.py createsuperuser
    ```
4. Run the project
    ```
      python manage.py runserver
    ```
