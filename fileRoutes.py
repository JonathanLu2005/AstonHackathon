from flask import render_template, Blueprint, request
import random

routeManager = Blueprint('routeManager', __name__, template_folder='templates', static_folder='static')

@routeManager.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

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

@routeManager.route('/joinRoom/<id>', methods=["POST","GET"])
def joinRoom(id):
    test = "hello"
    return render_template('joinRoom.html', {{test}})

@routeManager.route('/rooms', methods=["POST", "GET"])
def rooms():
    
    return render_template('rooms.html')

@routeManager.route('/getJson',methods=["POST","GET"])
def getJson():
    return {"hello":"parth"}
                    
@routeManager.route('/studyRoom', methods=["POST","GET"])
def studyRoom():
    roomName = request.form["roomName"]
    roomCode = request.form["roomCode"]
    return render_template('studyRoom.html',roomName = roomName, roomCode = roomCode)
#[{codes:...,name:...}...]
