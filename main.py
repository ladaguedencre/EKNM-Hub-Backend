from flask import Flask, abort
from flask_cors import CORS
from bindings import get_bindings
from goods import get_goods
from brews import get_brews
from articles import get_article

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EKNM Hub Backend. Leave if you don't know what you are doing."
    
@app.route("/api/bindings")
def bindings():
    return get_bindings()

@app.route("/api/goods")
def goods():
    return get_goods()

@app.route("/api/brews")
def brews():
    return get_brews()

@app.route('/api/articles/<id>')
def article(id: str):
    article = get_article(id)
    if not article:
        abort(404)
    return article
    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5003)