This is a Python webapp was for a project that had a vet prompt to build a web application that would help them manage their animals and vets (but instead of a vet, I've modelled it after a Pokémon Center).

Requirements:
```
Flask
Flask-Migrate
Jinja2
SQLAlchemy
postgresql
requests
```
These can be installed using pip (for example, the terminal command to install import would be 'pip3 import').

Set up:
1. First you need to set up a database called "pokecenter". In postgresql the command will be 'createdb pokecenter'. Go into app.py and on line 7 (app.config) and change the username to yours.

2. Initiate, migrate, and upgrade the models. Run the following commands (note, you will need to run these flask commands from the terminal in the relevant directory, which would be in the main folder which contains all the pokémon center files):
```
flask db init
flask db migrate
flask db upgrade
```

3. Run the seed files - in your Terminal (and again running within the main folder) and enter 'flask seed_pokédex' - this will fill up your pokédex table in your database with entries 1 to 1010 (i.e. all the currently available pokémon). Then run 'flask seed' - this will enter in some example entries for instances of pokémon, trainers and nurses.

Once you have done those steps, the application should be able to run, which is done by typing in 'flask run'. You will be able to open it in your browser entering in 'localhost:4999'. By default this webapp will run on port 4999, which can be changed from the .flaskenv file if something else is already using that port (just change FLASK_RUN_PORT to whichever port you desire).

Instructions for use:
There are 4 main links on the navbar:
"Home" will take you to the landing page

"Pokémon' will take you to a view of all the Pokémon, and where you can Register a new Pokémon to the Center. Please note that you will need to assign a trainer to the Pokémon, and said trainer will need to be assigned a Nurse.

"Trainers" will take you to a view of all trainers on the database. There will also be a button to Register a new Trainer on the database.

"Nurses" will take you to a view of all the Nurses (and again, you can create new nurses from the "register nurse" button on that page)

Each of the entries on each of these view pages can be accessed, where details can be edited or deleted.
