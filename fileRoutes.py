
from flask import render_template, Blueprint, request, url_for, redirect
from functions import addUniquePair, getActiveRooms, registerUser, loginUser
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from AI import generate_content
import random
import json

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
        return render_template('login.html', errorMessage="")
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = loginUser(username, password)

        if error != None:
            return render_template('login.html', errorMessage=error)
        else:
            return redirect(url_for('routeManager.rooms'))

@routeManager.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template('register.html', errorMessage="")
    
    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        error = registerUser(username, password)
        if error != None:
            return render_template('register.html', errorMessage=error)
        return redirect(url_for('routeManager.rooms'))

@routeManager.route('/rooms', methods=["POST", "GET"])
def rooms():
    return render_template('rooms.html', errorMessage="")

@routeManager.route('/getJson',methods=["POST","GET"])
def getJson():
    return getActiveRooms()

@routeManager.route('/studyRoom', methods=["GET"])
def studyRoom():
    roomName = request.args.get("roomName")
    roomCode = request.args.get("roomCode")
    return render_template('studyRoom.html', roomName = roomName, roomCode = roomCode)
                   
@routeManager.route('/studyRoomCreate', methods=["POST"])
def studyRoomCreate():
    roomName = request.form["roomName"]
    roomCode = addUniquePair(roomName)
    print("THE ROOM NAME IS ", roomName)
    print("THE ROOM CODE IS ", roomCode)
    return redirect(url_for('routeManager.studyRoom', roomName = roomName, roomCode = roomCode))

@routeManager.route('/studyRoomJoin', methods=["POST"])
def studyRoomJoin():
    roomCode = request.form["roomCode"]
    print("THE ROOM CODE IS ", roomCode)
    activeRooms = getActiveRooms()
    print(activeRooms)
    for room in activeRooms:
        if room['codes'] == roomCode.upper():
            return redirect(url_for('routeManager.studyRoom', roomName = roomName, roomCode = roomCode))
    return render_template('rooms.html', errorMessage="Room does not exist")

@routeManager.route('/studySpaceTest', methods=["POST","GET"])
def studySpaceTest():
    return render_template('studySpaceTest.html')

@routeManager.route('/promptAI', methods=["POST"])
def promptAI():
    template1 = "Generate 10 questions which relate to the below text. The questions should be multiple choice, each of which have 4 options. Give your output as a JSON object with all questions and answers.\n"
    prompt = request.form["prompt"]
    res = generate_content(template1+prompt)
    print(res[4:-4])
    return json.loads(res[4:-4])
    #return render_template('response.html', response=generate_content(prompt))
    