from db import db

class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256))
    
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    def __init__(self, text, article_id):
        self.text = text
        self.article_id = article_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "id": self.id,
            "comment:": self.text,
            "article_id:": self.article_id
        }