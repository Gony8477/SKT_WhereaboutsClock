import socket
import time
#from apscheduler.schedulers.background import BackgroundScheduler

HOST = "52.78.114.210"
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connection():
    while True:
        try:
            s.connect((HOST,PORT))
            break
        except:
            time.sleep(1)

#sched = BackgroundScheduler()

def sendingMsg():
    request = bytes('Request','utf-8')
    s.send(request)
    data = s.recv(1024)
    print("After recv")
    return data

def disconnectingSoc():
    s.close()

#sched.add_job(sendingMsg, 'interval', seconds=5)
#sched.start()
