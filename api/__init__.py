from flask import Flask

def create_app():
  app = Flask(__name__)
  from .routes.welcome import welcome_blueprint
  from .routes.animals import animals_blueprint
  from .routes.pet import pet_blueprint

  app.register_blueprint(welcome_blueprint)
  app.register_blueprint(animals_blueprint)
  app.register_blueprint(pet_blueprint)

  return app