__author__ = 'Administrator'

from application import db

class Image(db.Model, dict):
    __tablename__ = 'tblimage'
    image_id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(50))
    category = db.Column(db.String(50))
    size = db.Column(db.Integer)
    alt = db.Column(db.String(50))
    href = db.Column(db.String(150))
    image_save_name = db.Column(db.String(50))
    image_save_path = db.Column(db.String(50))
    fetch_sub = db.Column(db.Integer)

    def __init__(self, image_id):
        self.image_id = image_id

    def __repr__(self):
        return '<image %r>' % (self.image_id)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class SubImage(db.Model):

    __tablename__ = 'tblsubimage'
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer)
    img_url = db.Column(db.String(50))
    url = db.Column(db.String(150))
    image_save_name = db.Column(db.String(50))
    image_save_path = db.Column(db.String(50))
    alt = db.Column(db.String(50))

    def __init__(self, id):
        self.id = id

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

if __name__ == '__main__':
    print SubImage.query.get(2)