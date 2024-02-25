from pymongo import MongoClient
import random

currentActiveCodes = []
forumComments=["Wow! Much goos!"]
client = MongoClient('mongodb://localhost:27017/')

db = client["data"]
myUsers = db["myUsers"]
def addNewComment(newComment):
    forumComments.append(newComment)
def getForumComments():
    return forumComments
def getCurrentActiveCodes():
    return currentActiveCodes

def insertDataToDb():
    dataEx = {"name": "AstonHack2024", "password": "something"}
    myUsers.insert_one(dataEx)

def generateRoomCode():
    code = ""
    characterSet = {1: "A", 
            2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 
            16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: "0", 28: "1", 29: "2", 
            30: "3", 31: "4", 32: "5", 33: "6", 34: "7", 35: "8", 36: "9"}
    for i in range(0, 4):
        code = code + (characterSet[random.randint(1, 36)])
    print(code)
    return code

def addUniquePair(roomName):
    new_code = generateRoomCode()
    while True:
        flag = True
        for pair in currentActiveCodes:
            if pair["codes"] == new_code:
                flag = False
                break  # Break out of the for loop
        if flag:
            break  # Break out of the while loop if a unique code is found
        else:
            new_code = generateRoomCode()
    
    currentActiveCodes.append({"codes": new_code, "name": roomName})
    print("CURRENT ACTIVE CODES: ", currentActiveCodes)
    return new_code

def getActiveRooms():
    return currentActiveCodes

def registerUser(username, password):
    res = myUsers.find_one({"name": username})
    if res != None:
        return "User already exists!"
    else:
        dataToAdd = {"name": username, "password": password}
        myUsers.insert_one(dataToAdd)
        return None

def loginUser(username, password):
    res = myUsers.find_one({"name": username})
    if res == None:
        return "User does not exist!"
    else:
        if res["password"] != password:
            return "Incorrect password!"
        else:
            return None

