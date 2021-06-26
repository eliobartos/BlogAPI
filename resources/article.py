from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.article import ArticleModel

class Article(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=False, store_missing=False)
    parser.add_argument('date_created', type=str, required=False, store_missing=False)
    parser.add_argument('comments', action='append', type=str, required=False, store_missing=False)
    parser.add_argument('views', type=int, required=False, store_missing=False)

    parser_post = parser.copy()
    parser_post.replace_argument('name', type=str, required=True, help="Key name is missing and is required!")

    @jwt_required()
    def get(self, _id): 
        article = ArticleModel.find_by_id(_id)
        if article:
            return article.json()
        else:
            return {'message': 'Article not found!'}

    @jwt_required()
    def post(self, _id):
        if ArticleModel.find_by_id(_id) is not None:
            return {'message': f'Article with id: {_id} already exists!'}

        data = Article.parser_post.parse_args()
        article = ArticleModel(data['name'])
        article.save_to_db()
        return article.json()

    @jwt_required()
    def put(self, _id):
        article = ArticleModel.find_by_id(_id)
        if article is None:
            return {'message': f'Article with id: {_id} does not exist!'}

        data = Article.parser.parse_args()
        article.update(data)
        article.save_to_db()
        return article.json()

    @jwt_required()
    def delete(self, _id):
        article = ArticleModel.find_by_id(_id)
        if article:
            article.delete_from_db()
        return {'message': "Item Deleted!"}