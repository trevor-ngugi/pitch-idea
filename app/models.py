from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    posts = db.relationship("Post",backref = "posts",lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer,primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # comments = db.relationship("Comment",backref = "post_comments",lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_posts(cls,id):
        posts = Post.query.filter_by(user_id=id).all()
        return posts