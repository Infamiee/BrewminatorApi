import mysql.connector
from Parser import Parser
from os import listdir
from os.path import isfile, join
import os
import json
class Connector:
    def __init__(self):
        self.mydb = mysql.connector.connect (
            host="localhost",
            user="root",
            passwd="MEZCN0Mw",
            database="Brewminator")
        self.cursor = self.mydb.cursor()
        self.cursor.execute('''CREATE TABLE if not exists Recipe (
                               RecipeID int AUTO_INCREMENT PRIMARY KEY ,
                               RecipeName varchar(255) NOT NULL,
                               RecipeFileName varchar(255) NOT NULL 
                               );''')


    def update(self,data):
        sql = '''INSERT IGNORE INTO Recipe(RecipeName,RecipeFileName,Style)
        SELECT %s, %s,%s FROM DUAL 
    WHERE NOT EXISTS (SELECT * FROM Recipe 
      WHERE RecipeName=%s AND RecipeFileName=%s AND Style =%s LIMIT 1)'''
        self.mydb.cursor().execute(sql,data+data)
        self.mydb.commit()

    def get_recipes_by_id(self,id):
        sql = '''SELECT RecipeFileName FROM Recipe WHERE RecipeID = %s '''
        cursor = self.mydb.cursor()
        cursor.execute ( sql, (id,) )
        return cursor.fetchone()

    def save_all_recipes(self):
        parser = Parser()
        files = [f for f in listdir ( "./static/recipes/" ) if isfile ( join ( "./static/recipes/", f ) ) and os.path.splitext ( f ) [1] == ".xml"]
        for file in files:
            data = parser.get_parsed_recipe(file)
            name =data["RECIPES"]["RECIPE"]["NAME"]
            self.update((name,file[:-4]))



