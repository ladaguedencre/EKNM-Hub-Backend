from flask import Flask, abort
from flask_cors import CORS
from api.archive import api_get_article, api_get_bindings
from api.brews import api_get_brews
from api.goods import api_get_goods

app = Flask(__name__)
CORS(app)

# Routing layer

@app.route("/")
def route_home():
    return "EKNM Hub Backend is running"
    
@app.route("/api/bindings")
def route_bindings():
    return api_get_bindings()

@app.route("/api/goods")
def route_goods():
    return api_get_goods()

@app.route("/api/brews")
def route_brews():
    return api_get_brews()

@app.route('/api/archive/<arg>')
def route_archive(arg: any):
    return api_get_article(arg)

    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5003)