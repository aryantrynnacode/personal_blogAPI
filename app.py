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
        if not article:
                return jsonify({"error": "Article not found"}), 404
        return jsonify(article), 200

@app.route('/articles', methods=["POST"])
def add_articles():
    data = request.get_json()

    if not data or "article_title" not in data or "article_body" not in data:
        return jsonify({"error": "Invalid request body"}), 400

    title = data["article_title"].strip()
    content = data["article_body"].strip()

    article_id = create_article(title, content)

    return jsonify({
        "message": "Article created",
        "id": article_id
    }), 201

@app.route('/articles/<int:article_id>', methods = ["DELETE"])
def del_article(article_id):
        article = delete_article(article_id)
        return jsonify({"message": "article deleted"}),200

@app.route('/articles/<int:article_id>', methods = ["PUT"])
def upd_article(article_id):
        data = request.json
        title = data["new_title"]
        content = data["new_body"]

        update_article(article_id, title, content)
        return jsonify({"message": "article updated"}),200



        
