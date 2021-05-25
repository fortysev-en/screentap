import pyrebase
import os

firebaseConfig = {
    "apiKey": "AIzaSyAk0xzpUuH0LYXihigz3OXentCn1T8YC3Q",
    "authDomain": "global-testing-env.firebaseapp.com",
    "databaseURL": "https://global-testing-env-default-rtdb.firebaseio.com",
    "projectId": "global-testing-env",
    "storageBucket": "global-testing-env.appspot.com",
    "messagingSenderId": "403456253125",
    "appId": "1:403456253125:web:129423ef3a31c45a5a24ac"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

cloud_path = "images/stop_screentap.jpg"
local_path = ("stop_screentap.jpg")
storage.child(cloud_path).put(local_path)
print("Image Uploaded")
storage.child('images/stop_screentap.jpeg').download('', 'stop_screentap.jpeg')