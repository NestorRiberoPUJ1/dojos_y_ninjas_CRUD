from dojo_app.config.mysqlconnection import connectToMySQL


class Dojo:

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def muestraDojos(cls):
        query = "SELECT * FROM dojos_ninjas.dojos;"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        dojos = []
        for u in results:
            dojos.append(cls(u))
        return dojos