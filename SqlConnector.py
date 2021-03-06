import mysql.connector
from Parser import Parser
from os import listdir
from os.path import isfile, join
import os
import json
class Connector:
    def __init__(self):
        self.mydb = mysql.connector.connect (
            host="remotemysql.com",
            user="uNl4XTTb8s",
            passwd="1pe5PmTX3p",
            database="uNl4XTTb8s")
        self.cursor = self.mydb.cursor()
        self.cursor.execute('''CREATE TABLE if not exists Recipe (
                               RecipeID int AUTO_INCREMENT PRIMARY KEY ,
                               RecipeName varchar(255) NOT NULL,
                               RecipeFileName varchar(255) NOT NULL 
                               );''')


    def update(self,data):
        sql = '''INSERT IGNORE INTO Recipe(RecipeName,RecipeFileName)
        SELECT %s, %s FROM DUAL 
    WHERE NOT EXISTS (SELECT * FROM Recipe 
      WHERE RecipeName=%s AND RecipeFileName=%s LIMIT 1)'''
        self.cursor.execute(sql,data+data)
        self.mydb.commit()

    def get_recipes_by_id(self,id):
        sql = '''SELECT RecipeFileName FROM Recipe WHERE RecipeID = %s '''
        self.cursor.execute(sql,(id,))
        return self.cursor.fetchone()

    def save_all_recipes(self):
        parser = Parser()
        files = [f for f in listdir ( "./static/recipes/" ) if isfile ( join ( "./static/recipes/", f ) ) and os.path.splitext ( f ) [1] == ".xml"]
        for file in files:
            data = parser.get_parsed_recipe(file)
            data = json.loads(data)
            name =data["RECIPES"]["RECIPE"]["NAME"]
            self.update((name,file[:-4]))



