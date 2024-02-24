from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://astonHack2024:aStonHack24@astonhack2024.6kwduwc.mongodb.net/?retryWrites=true&w=majority&appName=AstonHack2024"

from fileRoutes import routeManager #Must be after app is defined
app.register_blueprint(routeManager)

if __name__ == '__main__':
    app.run(debug=True)
    