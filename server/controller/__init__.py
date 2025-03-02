from flask import Flask
from .article import article_controller 
from .testimonial import testimonial_controller

def add_controllers(app:Flask):
    app.register_blueprint(article_controller)
    app.register_blueprint(testimonial_controller)
