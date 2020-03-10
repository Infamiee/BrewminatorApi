from os import listdir
from os.path import isfile, join
import os
from .SqlConnector import Connector
import mysql.connector

class Recipe_parser():
    def __init__(self):
        self.path = "./recipes/"
        self.files = [f for f in listdir(self.path) if isfile(join("./recipes/", f)) and os.path.splitext(f)[1] == ".txt"]

    def get_data_from_file(self,filename):
        with open ( self.path + filename+".txt", "r" ) as f:
            reader = f.read ()
            data = reader.split ( "\n" )

        return data


