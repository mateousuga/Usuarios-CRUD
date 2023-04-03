from flask_app.config.mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
    
    @classmethod
    def save(cls, formulario):
        #formulario = {first_name: "Elena", last_name: "De Troya", email:"elena@codingdojo.com"}
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('crud_modularizado').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM users"
        results = connectToMySQL('crud_modularizado').query_db(query)
        #results = {
            #{id: 1, first_name:'helena', last_name:'de troya', email:'de troya@gmail.com'}}
        users = []
        for u in results: #u va a estar guardando mi diccionario
            user = cls(u) #user = User(u) -> me crea un objeto/instancia de User
            users.append(user)
        
        return users
    
    @classmethod
    def delete(cls, formulario):
        #formulari = {id:1}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('crud_modularizado').query_db(query, formulario)
        return result
    
    @classmethod
    def get_by_id(cls, formulario):
        #formulario = {id:1}
        query = "SELECT * FROM users WHERE id = %(id)s" #SELECT siempre regresa una lista
        result = connectToMySQL('crud_modularizado').query_db(query, formulario)
        #se recibe una lista con un diccionario result = [{id:1,first_name:'helena'.....}]
        diccionario = result[0]
        user = cls(diccionario) #user = User(diccionario) -> intancia/objeto de usuario
        return user
    
    @classmethod
    def update(cls, formulario):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('crud_modularizado').query_db(query, formulario)
        return result