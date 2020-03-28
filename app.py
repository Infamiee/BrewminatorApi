from flask import Flask
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
    except:
        return "Wrong parameter type",400
    try:
        filename = connector.get_recipes_by_id(arg)[0]
        data = parser.get_parsed_recipe ( filename )
        data = json.loads(data)
        data = data["RECIPES"]["RECIPE"]

    except:
        return "Recipe not found", 404
    return data,200


if __name__ == '__main__':
    app.run()


