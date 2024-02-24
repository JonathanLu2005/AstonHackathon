from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

from fileRoutes import routeManager #Must be after app is defined
app.register_blueprint(routeManager)

if __name__ == '__main__':
    app.run()
