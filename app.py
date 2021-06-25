from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from dotenv import load_dotenv
import os

from resources.article import Article
from resources.article_list import ArticleList
from resources.comment import Comment
from resources.user import UserRegister
from db import db

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Article, '/article/<int:_id>')
api.add_resource(ArticleList, '/articles')
api.add_resource(Comment, '/article/<int:_id>/comments')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    
    app.run(debug=True)