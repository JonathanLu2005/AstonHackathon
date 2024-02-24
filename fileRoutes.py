from flask import render_template, Blueprint, request
from functions import generateRoomCode 
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

@routeManager.route('/testing', methods=["POST", "GET"])
def testing():
    generateRoomCode()
    return "Done"


@routeManager.route('/getJson',methods=["POST","GET"])
def getJson():

    data = [{
            "name":"roomName",
            "codes": "XXXX"

            },
            {
            "name":"roomName",
            "codes": "XXXX"
            },
            {
                "name":"roomName",
                "codes": "XXXX"
            }
            
            ]

    return data