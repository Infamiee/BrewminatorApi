import os
from os import listdir
from os.path import isfile, join

from flask import Flask
from flask import request

from Parser import Parser
from flask_sqlalchemy import SQLAlchemy

app = Flask ( __name__ )
app.config.from_pyfile ( "config.cfg" )
db = SQLAlchemy ( app )
parser = Parser ()


class Recipe ( db.Model ):
    id = db.Column ( db.Integer, primary_key=True, autoincrement=True )
    name = db.Column ( db.Text, nullable=False )
    filename = db.Column ( db.Text, nullable=False )
    style = db.Column ( db.Text, nullable=False )


def setup():
    db.drop_all ()
    db.create_all ()
    files = [f for f in listdir ( "./static/recipes/" ) if
             isfile ( join ( "./static/recipes/", f ) ) and os.path.splitext ( f ) [1] == ".xml"]
    for file in files:
        data = parser.get_parsed_recipe ( file )
        name = data ["RECIPES"] ["RECIPE"] ["NAME"]
        style = data ["RECIPES"] ["RECIPE"] ["STYLE"] ["NAME"]
        x = Recipe ( name=name, filename=file, style=style )
        db.session.add ( x )

    db.session.commit ()


@app.route ( '/recipe', methods=["GET"] )
def get_recipe():
    arg = request.args.get ( "id" )
    if arg == None:
        return "Wrong parameter", 400
    try:
        arg = int ( arg )
    except Exception as e:
        return "Wrong parameter type", 400
    try:
        data = Recipe.query.filter_by ( id=arg ).first ()

        data = parser.get_parsed_recipe ( data.filename )


    except Exception as e:
        raise e
        return "Recipe not found", 404
    return data, 200


@app.route ( '/recipe/all', methods=["GET"] )
def get_recipes():
    recipes = Recipe.query.all();
    ret = {}
    for recipe in recipes:

        ret[recipe.id] = {
            "name":recipe.name,
            "style":recipe.style
        }

    return ret


with app.app_context ():
    setup()







