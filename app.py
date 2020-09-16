from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
