from myapp import db

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(128))
    core = db.Column(db.Integer)

class WebpageInfo(db.Model):
    __tablename__ = 'webpage_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    h1_titles = db.Column(db.Text)
    distinct_link_domains = db.Column(db.Text)
    screenshot_path = db.Column(db.String(255))
    minio_path = db.Column(db.String(255))

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(website_url=url).first()
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
