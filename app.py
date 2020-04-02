from flask import Flask,jsonify
from flask import request
from SqlConnector import Connector
from Parser import Parser
import json

app = Flask ( __name__ )


connector = Connector()
parser = Parser()

@app.route ( '/recipe', methods=["GET"] )
def get_recipe():

    arg = request.args.get("id")
    if arg == None:
        return "Wrong parameter",400

    try:
        arg = int(arg)
    except Exception as e:
        return "Wrong parameter type",400
    try:
        filename = connector.get_recipes_by_id(arg)[0]
        data = parser.get_parsed_recipe ( filename )

        data = data["RECIPES"]["RECIPE"]
        print(data)
    except Exception as e:
        raise e
        return "Recipe not found", 404
    return data,200


@app.route ( '/recipe/all', methods=["GET"] )
def get_recipes():
    recipes = connector.get_all_recipe()
    ret = {}
    for recipe in recipes:
        id,name,style = recipe

        ret[id] = {
            "name":name,
            "style":style
        }

    return ret


if __name__ == '__main__':
    app.run()


