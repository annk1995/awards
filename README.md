# Moringa Awards


#### By 


## Description


## User Stories
As a user, I would like to be able to do the following:
* Post a project to be rated/reviewed.
* Rate/ review other users' projects.
* Search for projects.
* View projects overall score.
* View my profile page.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
| Display all projects | On home page load | Loads all the available projects |
| New User Project | Click New Project button from navbar | User redirected to new post page with forms for new project, which when filled redirects to home page with the new project  |
| User registration | Fill required fields and click on register button | User's info is registered to the database and user is redirected to home page |
| User login | Fill required fields and click on login button | User's info is confirmed with the database and user is redirected to home page, else if info doesn't match db records user is not able to login and access the home page |


## Setup/Installation Requirements
To clone this repo, open terminal in your desired folder then run:

        $ git clone 
        $ cd /moringa-awards

To create and activate the virtual environment and install pip:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python


To install all the required pip modules for proper functionality:

        (virtual)$ python3.6 -m pip install -r requirements.txt

To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
To run unittests:

        $ python3.6 manage.py test awardsapp

## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Django v 2.2.3
* Bootstrap4
* Django-registration v 3.0.1
* Postgres Database
* gunicorn


## Contributors


## Support and contact details
To support me, you can contact me at

## License

