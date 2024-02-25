from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017"

from fileRoutes import routeManager #Must be after app is defined
app.register_blueprint(routeManager)

if __name__ == '__main__':
    app.run(debug=True)
    