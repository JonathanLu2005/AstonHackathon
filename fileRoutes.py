from flask import render_template, Blueprint, request
from dbFunctions import insertData
import random
import json

routeManager = Blueprint('routeManager', __name__, template_folder='templates', static_folder='static')

@routeManager.route('/', methods=["POST", "GET"])
def index():
    return render_template('baseHtml.html')

@routeManager.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # This is where you handle login
        return render_template('login.html')

@routeManager.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        # This is where you handle registration
        return render_template('register.html')

@routeManager.route('/joinRoom', methods=["POST", "GET"])
def joinRoom():
    return render_template('joinRoom.html')

@routeManager.route('/testing', methods=["POST", "GET"])
def createRoom():
    insertData()
    return "This is a test page"

@routeManager.route('/getJsonData', methods=["POST", "GET"])
def getJsonData():
    exampleData = {{}}
    return "This is a test page"