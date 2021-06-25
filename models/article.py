from db import db
import datetime as dt


class ArticleModel(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    views = db.Column(db.Integer)

    comments = db.relationship('CommentModel')

    def __init__(self, name):
        self.name = name
        self.date_created = dt.datetime.today()
        self.views = 0

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_created': self.date_created.strftime('%Y-%m-%d'),
            'views': self.views,
            'comments': [comment.json() for comment in self.comments]
            }

    def get_all_comments(self):
        return [comment.json() for comment in self.comments]

    def update(self, data):
        if 'views' in data.keys():
            self.views = data['views']

        if 'name' in data.keys():
            self.name = data['name']
    
        if 'date_created' in data.keys():
            self.date_created = dt.datetime.strptime(data['date_created'], '%Y-%m-%d')