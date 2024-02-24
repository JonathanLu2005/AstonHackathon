import os
import json
from flask import Flask, url_for, jsonify
from flask import render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos

allRoomCodes = [""]

def create_app():
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # login, signup, main home page 
    # some page to generate code and meetup w ppl for call

    # place for game

    # SIGNIN
    @app.route("/", methods=["POST","GET"])
    def signIn():
        # if data matches
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
                redirect(url_for("joinRoom"))

            else:
                return render_template("login.html")

        return render_template("login.html")
    
    # REGISTER
    @app.route("/register", methods=["POST","GET"])
    def register():
        if request.method == "POST":
            Username = request.form["username"]
            Password = request.form["password"]

            # add data to database


            addUser = {"Username" : Username, "Password" : Password}  
            x = myUsers.insert_one(addUser)              

            redirect(url_for("MainPage"))

        return render_template("siginIn.html")

    # joinroom (code generator, make call with people)

    # create button -> creates code
    # list of rooms
    # accept in a room code

    @app.route("/joinRoom", methods=["POST","GET"])
    def joinRoom():    
        # joining room
        global allRoomCodes

        if request.method == "POST" and "roomCode" in request.form:
            roomCode = request.form["roomCode"]

            if roomCode in allRoomCodes:
                redirect(url_for("/joinRoom/{{roomCode}}"))

        elif request.method == "POST":
            characterSet = {1: "A", 
            2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 
            16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: "0", 28: "1", 29: "2", 
            30: "3", 31: "4", 32: "5", 33: "6", 34: "7", 35: "8", 36: "9"}

            while (generateRoomCode not in allRoomCodes): 
                generateRoomCode = ""
                randomCode = []

                for i in range(0, 4):
                    randomCode.append(characterSet.get(random.randint(1,36)))

                generateRoomCode = "".join([str(item) for item in randomCode])

            allRoomCodes.append(generateRoomCode)

            redirect(url_for("/joinRoom/{{generateRoomCode}}"))

        jsonAllRoomCodes = json.dumps(allRoomCodes)
        getJsonData(jsonAllRoomCodes)
        return render_template("joinRoom.html")

    @app.route("getJsonData", methods=["GET"])
    def getJsonData(data):
        return data

    @app.route("/joinRoom/<id>", methods=["POST","GET"])
    def joinRoom(id):
        


        
        return render_template("joinRoom.html")

    return app