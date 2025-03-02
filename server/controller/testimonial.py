from flask import Blueprint, jsonify, abort
from server.dbClient import get_cursor
import server.service.testimonial as testimonial_service

testimonial_controller = Blueprint('testimonial', __name__, url_prefix='/api/testimonial')
@testimonial_controller.route('/random')
def random_testimonial():
    res = []
    with get_cursor() as db:
        res = testimonial_service.random_testimonial(db)
    return jsonify(res) if res is not None else abort(500)
