from pymongo import MongoClient 

client = MongoClient('mongodb+srv://astonHack2024:aStonHack24@astonhack2024.6kwduwc.mongodb.net/?retryWrites=true&w=majority&appName=AstonHack2024')

db = client["data"]
myUsers = db["myUsers"]

def insertData():
    dataEx = {"name": "AstonHack2024", "password": "something"}
    myUsers.insert_one(dataEx)

"""
{
    #Study sets 
    {
        "name": "set1",
        "data": {
                    {
                        "question":"this is question",
                        "answer": {
                            "answer1": "this is answer",
                            "answer2": "this is answer",
                            "answer3": "this is answer",
                            "answer4": "this is answer"
                        }
                    },
                    {
                        "question":"this is question",
                        "answer":"this is answer"
                    },
                    {
                        "question":"this is question",
                        "answer":"this is answer"
                    }

                }
    }

    {
        "name": "set1",
        "data": {
                    {
                        "question":"this is question",
                        "answer":"this is answer"
                    },
                    {
                        "question":"this is question",
                        "answer":"this is answer"
                    },
                    {
                        "question":"this is question",
                        "answer":"this is answer"
                    }

                }
    }
}

"""