from flask import render_template, Blueprint, request
from functions import addUniquePair, getActiveRooms
import random

routeManager = Blueprint('routeManager', __name__, template_folder='templates', static_folder='static')

@routeManager.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

@routeManager.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        Username = request.form["username"]
        Password = request.form["password"]

            # check if username and password matches

        myquery = { "Username" : Username, "Password" : Password}
        results = myUsers.find(myquery)

        ifAccountExist = 0

        for x in results:
            ifAccountExist += 1

        if ifAccountExist > 0:
                # database code here to check if details exist in database
            redirect(url_for("rooms"))

        else:
            return render_template("login.html")

    return render_template("login.html")
"""
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # This is where you handle login
        return render_template('login.html')"""

@routeManager.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        Username = request.form["username"]
        Password = request.form["password"]

            # add data to database


        addUser = {"Username" : Username, "Password" : Password}  
        x = myUsers.insert_one(addUser)              

        redirect(url_for("rooms"))

    return render_template("register.html")
    """
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        # This is where you handle registration
        return render_template('register.html')
    """

@routeManager.route('/rooms', methods=["POST", "GET"])
def rooms():
    
    return render_template('rooms.html', errorMessage="")

@routeManager.route('/getJson',methods=["POST","GET"])
def getJson():
    return getActiveRooms()
                    
@routeManager.route('/studyRoomCreate', methods=["POST","GET"])
def studyRoom():
    roomName = request.form["roomName"]

    ##Call the fnuction to generate a unique code
    roomCode = addUniquePair(roomName)

    print("THE ROOM NAME IS ", roomName)
    print("THE ROOM CODE IS ", roomCode)
    ##Add the code and name to aactive array - TO DO
    return render_template('studyRoom.html',roomName = roomName, roomCode = roomCode)
#[{codes:...,name:...}...]

@routeManager.route('/studyRoomJoin', methods=["POST","GET"])
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