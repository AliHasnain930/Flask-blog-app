from flask import Flask, render_template, url_for, redirect
from datetime import datetime
from form import NewBlogForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'my_secret_key'

blogs = [
    {
        "id": 1,
        "title": "Blog Post 1",
        "content": "This is blog post 1",
        "author": "Ali Hasnain",
        "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
    },
    {
        "id": 2,
        "title": "Blog Post 2",
        "content": "This is blog post 2",
        "author": "Ali Hasnain",
        "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
    },
    {
        "id": 3,
        "title": "Blog Post 3",
        "content": "This is blog post 3",
        "author": "Abdul Momin",
        "created_at": datetime.today().strftime("%b %d %Y %H:%M:%S")
    },
]


@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)


@app.route('/new-blog', methods=['GET', 'POST'])
def new_blog():
    form = NewBlogForm()
    if form.validate_on_submit():
        print("Post created successfully")
        return redirect(url_for('index'))
    return render_template('newBlog.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
