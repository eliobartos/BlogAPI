from flask_jwt import jwt_required
from flask_restful import Resource

from models.article import ArticleModel

class ArticleList(Resource):
    @jwt_required()
    def get(self):
        return {'articles': [article.json() for article in ArticleModel.query.all()]}


