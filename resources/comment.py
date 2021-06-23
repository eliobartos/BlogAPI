from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

from models.comment import CommentModel
from models.article import ArticleModel

class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('comment', required=True, type=str, help="Payload must contain comment key of type string!")

    @jwt_required()
    def get(self, _id):
        article = ArticleModel.query.filter_by(id=_id).first()
        
        if article:
            return {'comments': article.get_all_comments()}
        else:
            return {'message': 'Article not found!'}

    @jwt_required()
    def post(self, _id):
        article = ArticleModel.query.filter_by(id=_id).first()

        data = Comment.parser.parse_args()

        if article:
            comment = CommentModel(data['comment'], _id)
            comment.save_to_db()
            return comment.json()
        else:
            return {'message': 'Article not found!'}