import xmltodict,json

class Parser:
    def __init__(self):
        self._path = "./static/recipes/"



    def get_parsed_recipe(self,filename):
        print(filename)
        try:
            with open(self._path+filename+".xml","r") as f:
                data = xmltodict.parse(f.read())

                return data
        except Exception as e:
            raise e