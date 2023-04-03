#importacion de Flask
from flask_app import app

#importacion controladores
from flask_app.controllers import user_controller

#ejecucion de la app
if __name__ == '__main__':
    app.run(debug=True)