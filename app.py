from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jamesdickson@localhost:5432/pokecenter"
# app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)
from seed_pokédex import seed_pokedex
app.cli.add_command(seed_pokedex)

from controllers.pokémon_controller import pokémon_blueprint
from controllers.nurse_controller import nurses_blueprint
from controllers.trainer_controller import trainers_blueprint

app.register_blueprint(pokémon_blueprint)
app.register_blueprint(nurses_blueprint)
app.register_blueprint(trainers_blueprint)

@app.route("/")
def home():
    return render_template('index.jinja')