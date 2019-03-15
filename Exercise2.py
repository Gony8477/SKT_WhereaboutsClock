import RPi.GPIO as GPIO
import time

def sendSignal() :
    for k in range(4):
        GPIO.output(pins[k], signal[step][k])

def numbertest(Pin_number):
    if Pin_number == 'Father':
            Pin_Number=1
            return Pin_Number
    if Pin_number == 'Mother':
            Pin_Number=2
            return Pin_Number

def locationtest1(Pin_location):
    if Pin_location == 'School':
            Pin_now_Location=1
            return Pin_now_Location
    if Pin_location  == 'Bookstore':
            Pin_now_Location=2
            return Pin_now_Location
    if Pin_location == 'Hospital':
            Pin_now_Location=3
            return Pin_now_Location
    if Pin_location == 'home':
            Pin_now_Location=4
            return Pin_now_Location

def locationtest2(Pin_now_Location):
    if Pin_past_Location == Pin_now_Location:
            return Pin_past_Location
    else:
            return Pin_now_Location
    Pin_past_Location = Pin_now_Location

def location_angle(Pin_past_Location, Pin_now_Location):
    if Pin_past_Location < Pin_now_Location:
         Answer= Pin_now_Location - Pin_past_Location
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

             
data0 = 'Father'
data1 = 'Bookstore'
        
Pin_number = data0
Pin_location = data1
numbertest(Pin_number)
locationtest1(Pin_location)
locationtest2(Pin_now_Location)
location_angle(Pin_past_Location, Pin_now_Location)


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






 
