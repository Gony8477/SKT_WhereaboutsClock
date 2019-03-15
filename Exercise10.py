import Desktop.Software_Engineering.SocketToReceiverTest_Client as Sock
import RPi.GPIO as GPIO
import time

def sendSignal() :
    for k in range(4):
        GPIO.output(pins[k], signal[step][k])

def numbertest(Pin):
    if Pin == 'Father':
          Pin=1
    elif Pin == 'Mother':
          Pin=2
          
def test1(Location):
    Now_Locate=0
    if Location == 'ITBT':
          Now_Locate=1
    if Location == 'Home':
          Now_Locate=2
    if Location == 'Playground':
          Now_Locate=3
    if Location == 'School':
          Now_Locate=4

def test2(Past_Locate,Now_Locate):
    if Past_Locate == Now_Locate:
        return Past_Locate
    else:
        return Past_Locate
    Past_Locate  = Now_Locate


def Angletest1(Past_Locate, Now_Locate):
    if Past_Locate < Now_Locate:
        Answer= Now_Locate - Past_Locate
        if Answer ==1:
            Answer_range=128
            return Answer_range
        elif Answer ==2:
            Answer_range=256
            return Answer_range
        elif Answer ==3:
            Answer_range=384
            return Answer_range
    elif Pin_past_Location > Pin_now_Location:
        Answer= Pin_past_Location - Pin_now_Location
        if Answer== 1:
             Answer_range=384
             return Answer_range
        elif Answer==2:
             Answer_range=256
             return Answer_range
        elif Answer ==3:
             Answer_range=128
             return Answer_range
    elif Pin_past_Location == Pin_now_Location:
         Answer_range =0
         return Answer_range

a = Sock.sendingMsg().split()
    
Pin= 'Father'
Location = a[0]
Past_Locate =0

numbertest(Pin)
test1(Location)
test2(Now_Locate)
location_angle(Past_Locate, Now_Locate)


if Pin_Number== 1:
    GPIO.setmode(GPIO.BCM)
    pins = [12,16,20,21]
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)
    FULL_STEP = 4
    HALF_STEP = 8
    signal_full = [
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              ]
    signal_half = [
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
              [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
              [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              ]
    steps = FULL_STEP
    signal = signal_full
    clockwise = True
    try:
        for i in range(Answer_range):
            if clockwise :
                for step in range(steps):
                    sendSignal()
                    time.sleep(0.01)
            else :
                for step in reversed(range(steps)):
                    sendSignal()
                    time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nInterrupted!")
    finally:
        GPIO.cleanup()

if Pin_Number==2:
    GPIO.setmode(GPIO.BCM)
    pins = [6,13,19,26]
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)
    FULL_STEP = 4
    HALF_STEP = 8
    signal_full = [
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              ]
    signal_half = [
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
              [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
              [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
              [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
              [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
              ]
    steps = FULL_STEP
    signal = signal_full
    clockwise = True
    try:
        for i in range(Answer_range):
            if clockwise :
                for step in range(steps):
                    sendSignal()
                    time.sleep(0.01)
            else :
                for step in reversed(range(steps)):
                    sendSignal()
                    time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nInterrupted!")
 
    finally:
        GPIO.cleanup() 
