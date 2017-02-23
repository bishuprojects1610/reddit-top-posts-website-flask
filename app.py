#!/usr/bin/env python3

from flask import Flask, render_template
from mongoengine.connection import connect
from data_model import Post


app = Flask(__name__)

@app.route("/")
def get_top_posts():
    # connect to db
    MONGO_URI = 'mongodb://localhost:27017'
    connect('sivji-sandbox', host=MONGO_URI)

    ## get the last date the webscraper was run
    for post in Post.objects().fields(date=1).order_by('-date').limit(1):
        day_to_pull = post.date.date()

    # return render_template('template.html', Post=Post, day_to_pull=day_to_pull)
    return render_template(
        'template.html',
        Post=Post,
        day_to_pull=day_to_pull)

if __name__ == "__main__":
    app.run()
