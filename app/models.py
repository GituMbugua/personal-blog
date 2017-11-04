from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255), index = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))   
    blogs =  db.relationship('Blog', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    # define relationship to Role via UserRoles
    roles = db.relationship('Role', secondary = 'user_roles')    

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), index = True)

# UserRoles association table
class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    image_path = db.Column(db.String())
    title = db.Column(db.String(255), index = True)
    post = db.Column(db.String(), index = True)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    photos = db.relationship('Photo', backref = 'blog', lazy = 'dynamic')
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blog = Blog.query.order_by(Blog.time.desc()).all()
        return blog
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    post_comment = db.Column(db.String(255), index = True)
    time = db.Column(db.DateTime, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
