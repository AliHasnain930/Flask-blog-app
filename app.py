from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from form import NewBlogForm

# configurations
app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# blogs = [
#     {
#         "id": 1,
#         "title": "Blog Post 1",
#         "content": "This is blog post 1",
#         "author": "Ali Hasnain",
#         "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
#     },
#     {
#         "id": 2,
#         "title": "Blog Post 2",
#         "content": "This is blog post 2",
#         "author": "Ali Hasnain",
#         "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
#     },
#     {
#         "id": 3,
#         "title": "Blog Post 3",
#         "content": "This is blog post 3",
#         "author": "Abdul Momin",
#         "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
#     },
# ]

# models


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    blogs = db.relationship('Blog', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.id} {self.name} {self.email})"


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.today)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Blog({self.id} {self.title} {self.created_at})"

# routes


@app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)


@app.route('/new-blog', methods=['GET', 'POST'])
def new_blog():
    form = NewBlogForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        content = form.content.data
        author_id = User.query.filter_by(name=author).first().id
        blog = Blog(title=title, content=content, author_id=author_id)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('newBlog.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
