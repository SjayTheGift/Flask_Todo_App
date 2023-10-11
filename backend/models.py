from database import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)

    def json(self):
        return {'id': self.id,'title': self.title, 'is_complete': self.is_complete}

    def __repr__(self):
        return '<Todos %r>' % self.title
        