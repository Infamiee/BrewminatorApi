from flask import Flask
from flask import request
from SqlConnector import Connector
import Parser
app = Flask ( __name__ )
from Parser import Parser

connector = Connector()
parser = Parser()

@app.route ( '/recipe', methods=["GET"] )
def get_recipe():

    arg = request.args.get("id")
    try:

        filename = connector.get_recipes_by_id(arg)[0]
    except:
        return "Recipe not found", 400
    print(filename)
    data =parser.get_parsed_recipe(filename)

    return data,200


if __name__ == '__main__':
    app.run()


