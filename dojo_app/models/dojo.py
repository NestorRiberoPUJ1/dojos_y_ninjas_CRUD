from dojo_app.config.mysqlconnection import connectToMySQL
from dojo_app.models.ninja import Ninja

class Dojo:

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas=[]

    @classmethod
    def muestraDojos(cls):
        query = "SELECT * FROM dojos_ninjas.dojos;"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        dojos = []
        for u in results:
            dojos.append(cls(u))
        return dojos

    @classmethod
    def createDojo(cls,form):
        query = "INSERT INTO dojos_ninjas.dojos (name) VALUES (%(name)s)"
        result = connectToMySQL("dojos_ninjas").query_db(query,form)
        return result

    @classmethod
    def cargaDojo(cls,form):
        query = "SELECT * FROM dojos_ninjas.dojos WHERE dojos.id = %(id)s ;"
        result = connectToMySQL("dojos_ninjas").query_db(query,form)
        dojo = result[0]
        dojo = cls(dojo)
        form={"id":dojo.id}
        dojo.ninjas=Ninja.muestraNinjas(form)
        return dojo