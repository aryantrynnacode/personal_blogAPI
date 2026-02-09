from flask import Flask, jsonify, request
from database import engine, MetaData
from blog_logic import get_all_articles, create_article, delete_article, update_article, get_article_by_id
import models

app = Flask(__name__)
@app.route('/articles', methods = ["GET"])
def getall_articles():
        article = get_all_articles()
        return jsonify(article)

@app.route('/articles/<int:article_id>', methods = ["GET"])
def get_articles(article_id):
        article = get_article_by_id(article_id)
        return jsonify(article)

@app.route('/articles', methods = ["POST"])
def add_articles():
        data = request.json
        title = data["article_title"]
        content = data["article_body"]
        create_article(title, content)
        return jsonify({"message": "article created"}),201

@app.route('/articles/<int:article_id>', methods = ["DELETE"])
def del_article(article_id):
        article = delete_article(article_id)
        return jsonify(article)

@app.route('/articles/<int:article_id>', methods = ["PUT"])
def upd_article(article_id):
        data = request.json
        title = data["new_title"]
        content = data["new_body"]

        update_article(article_id, title, content)
        return jsonify({"message": "article updated"}),200



        
