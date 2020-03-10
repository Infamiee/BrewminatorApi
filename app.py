from flask import Flask
from parser import Recipe_parser
app = Flask ( __name__ )
parser = Recipe_parser

@app.route ( '/' )
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run ()
