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

from controllers.pokémon_controller import pokémon_blueprint
from controllers.nurse_controller import nurses_blueprint

app.register_blueprint(pokémon_blueprint)
app.register_blueprint(nurses_blueprint)

@app.route("/")
def home():
    return render_template('index.jinja')