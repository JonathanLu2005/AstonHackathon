
from flask import render_template, Blueprint, request
from functions import addUniquePair, getActiveRooms
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import random

routeManager = Blueprint('routeManager', __name__, template_folder='templates', static_folder='static')
loginManager= LoginManager()
def initLoginManager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'routeManager.login'

@loginManager.user_loader
def load_user(user_id):
    return User.get(user_id)

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

@routeManager.route('/rooms', methods=["POST", "GET"])
def rooms():
    return render_template('rooms.html', errorMessage="")

@routeManager.route('/getJson',methods=["POST","GET"])
def getJson():
    return getActiveRooms()

@routeManager.route('/studyRoom', methods=["GET"])

                   
@routeManager.route('/studyRoomCreate', methods=["POST"])
def studyRoomCreate():
    roomName = request.form["roomName"]

    ##Call the fnuction to generate a unique code
    roomCode = addUniquePair(roomName)

    print("THE ROOM NAME IS ", roomName)
    print("THE ROOM CODE IS ", roomCode)
    ##Add the code and name to aactive array - TO DO
    return render_template('studyRoom.html',roomName = roomName, roomCode = roomCode)
#[{codes:...,name:...}...]

@routeManager.route('/studyRoomJoin', methods=["POST"])
def studyRoomJoin():
    roomCode = request.form["roomCode"]
    print("THE ROOM CODE IS ", roomCode)
    ##Check if the code exists in the active array - TO DO
    activeRooms = getActiveRooms()
    print(activeRooms)
    for room in activeRooms:
        if room['codes'] == roomCode.upper():
            return render_template('studyRoom.html',roomName = room["name"], roomCode = roomCode)
    return render_template('rooms.html', errorMessage="Room does not exist")

@routeManager.route('/studySpaceTest', methods=["POST","GET"])
def studySpaceTest():
    return render_template('studySpaceTest.html')