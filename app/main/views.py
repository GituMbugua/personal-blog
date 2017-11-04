from flask import render_template, redirect, url_for
from . import main
from .forms import BlogForm
from ..models import User, Blog
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    view route page function that returns index page
    '''
    blog = Blog.get_blogs()

    title = 'Home'
    return render_template('index.html', title = title, blog = blog)

@main.route('/blog/new', methods = ["GET", "POST"])
# @login_required
def new_blog():
    '''
    view category that returns a form to write a blog post
    '''
    form = BlogForm()
    # user = User.query.filter_by(id = id).first()
    if form.validate_on_submit():
        title = form.title.data
        image = form.image.data
        post = form.post.data

        # create blog post instance
        new_blog = Blog(title = title, image_path = image, post = post)

        # save blog
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = form)

