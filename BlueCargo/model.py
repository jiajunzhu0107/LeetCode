from portApi import db


class Port(db.Model):


    __tablename__ = "port"

    portId = db.Column(db.String(50), primary_key=True)
    # userId = db.Column(db.Integer, db.ForeignKey('user.userId'),
    #     nullable=False)
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy=True))
    name = db.Column(db.String(255), unique=False, nullable=True)
    country = db.Column(db.String(255), unique=False, nullable=True)
    data =  db.Column(db.String(255), unique=False, nullable=True)

    # def __repr__(self):
    #     return '<Port %r>' % self.name