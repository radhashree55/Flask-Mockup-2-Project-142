from flask import Flask, jsonify, request
import csv

allArticles = []

with open("shared_articles.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

likedArticles = []
notLikedArticles = []

app = Flask(__name__)


@app.route("/getArticle")
def getArticle():
    return jsonify({
        "data": allArticles[0],
        "status": "success"
    })


@app.route("/likedArticle", methods=["POST"])
def likedArticle():
    article = allArticles[0]
    likedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/unlikedArticle", methods=["POST"])
def unlikedArticle():
    article = allArticles[0]
    notLikedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run()
