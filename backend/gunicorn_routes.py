from flask import Blueprint

gunicorn_blueprint = Blueprint('gunicorn', __name__)

@gunicorn_blueprint.route('/gunicorn')
def gunicorn_route():
    return 'Hello from Gunicorn!'
