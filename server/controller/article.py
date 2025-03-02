from flask import Blueprint, jsonify, abort
from server.dbClient import get_cursor
import server.service.article as articleService

article_controller = Blueprint('article', __name__, url_prefix='/api/article')
released_articles = None
@article_controller.route('/')
def article_list():
    res = []
    with get_cursor() as db:
        res = articleService.article_list(db, released_articles)
    return jsonify(res) if res is not None else abort(500)

@article_controller.route('/<id>')
def article(id):
    res = None
    with get_cursor() as db:
        res = articleService.article(db, id, released_articles)
    return jsonify(res) if res is not None else abort(500)
