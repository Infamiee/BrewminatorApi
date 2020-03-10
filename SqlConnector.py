import mysql.connector


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
        VALUES (%s,%s)'''
        self.cursor.execute(sql,data)
        self.mydb.commit();

    def get_recipes_by_filename(self,name):
        sql = '''SELECT RecipeFileName FROM Recipe WHERE RecipeName LIKE  '%' %s '%' '''
        n = (name,)
        self.cursor.execute(sql,n)
        return self.cursor.fetchall()

