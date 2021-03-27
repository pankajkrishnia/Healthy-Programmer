# =============================Healthy Programmer================================
# In a 9-5 job, to drink 3.5 liters of water, one has to drink water every 32 minutes.
# Eye exercises have to be done every 30-40 minutes.
# Physical activity have to be done every 45-50 minutes..
from pygame import mixer
from datetime import datetime
from time import time

# Function for playing sounds for alert
def playingMusic(audio,stopAudio):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play(-1)
    while True:
        a = input()
        if a==stopAudio:
            mixer.music.stop()
            break

# Function to manage the Logs for the same
def myLogs(message):
    with open("mylogs.txt","a") as f:
        f.write(f"{message} {datetime.now()}\n")

# Main
if __name__ == '__main__':
    initial_exercise = initial_eyes = initial_water = time()
    # initial_eyes = time()
    # initial_exercise = time()
    water, eyes, exercise = 60*32, 35*60, 50*60  #in minutes
    # water = 10 # seconds
    # eyes = 30 # seconds
    # exercise = 50 # seconds
    print("==================HEALTHY PROGRAMMER==================")
    print("Welcome to Your Desk")

    while True:

        if time() - initial_water > water:
            print("This is your water drinking time --- Enter [drank] to stop the alarm")
            playingMusic("water.wav","drank")
            initial_water = time()
            myLogs("Drank Water at")

            if input("Enter Q to Exit OR Press any Key to Continue\n")=="Q":
                print("*****************Come back tomorrow :)*****************")
                break

        if time() - initial_eyes > eyes:
            print("This is your Eyes Exercise time --- Enter [eydone] to stop the alarm")
            playingMusic("eyes.wav","eydone")
            initial_eyes = time()
            myLogs("Done Eyes exercise at")

            if input("Enter Q to Exit OR Press any Key to Continue\n") == "Q":
                print("*****************Come back tomorrow :)*****************")
                break

        if time() - initial_exercise > exercise:
            print("This is your water drinking time --- Enter [exdone] to stop the alarm")
            playingMusic("physical.wav","exdone")
            initial_exercise = time()
            myLogs("Done Physical exercise at")

            if input("Enter Q to Exit OR Press any Key to Continue\n") == "Q":
                print("*****************Come back tomorrow :)*****************")
                break













