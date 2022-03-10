from dojo_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def muestraNinjas(cls,form):
        query = "SELECT * FROM dojos_ninjas.ninjas WHERE ninjas.dojo_id = %(id)s ;"
        results = connectToMySQL("dojos_ninjas").query_db(query,form)
        ninjas = []
        for u in results:
            ninjas.append(cls(u))
        return ninjas

    @classmethod
    def createNinja(cls,form):
        query = "INSERT INTO dojos_ninjas.ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        result = connectToMySQL("dojos_ninjas").query_db(query,form)
        return result
