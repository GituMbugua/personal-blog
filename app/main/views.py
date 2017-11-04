from flask import render_template, request, redirect, url_for
from . import main
from .forms import BlogForm
from ..models import User, Blog, Comment
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    view route page function that returns index page
    '''
    blogs = Blog.get_blogs()

    title = 'Home'
    return render_template('index.html', title = title, blogs = blogs)

@main.route('/blog/<int:id>', methods = ["GET", "POST"])
def blog(id):
    '''
    route to display a particular blog
    '''
    # display blog
    blog = Blog.query.get(id)


    # get info from comment form
    name = request.args.get('name')
    email = request.args.get('email')
    comment = request.args.get('comment')

    if comment:
        # comment instance
        new_comment = Comment(blog_id = blog.id, name = name, email = email, post_comment = comment)

        # save comment
        new_comment.save_comment()
        return redirect(url_for('.blog', id = blog.id))

    # display comments
    comments = Comment.get_comments(blog.id)

    title = 'Blog post'
    return render_template('blog.html', blog = blog, title = title, comment_form = form, comments = comments)

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