import RPi.GPIO as GPIO
import time
import MySQLdb

db=MySQLdb.connect('localhost','root','1234567890','TestDB')
# prepare a cursor object using cursor() method
cursor =db.cursor()
# execute SQL query using execute() method
#
cursor.execute("select * from TestStatus WHERE Pin=1 or Pin=2")

try:
    # Fetch a single row using fetchome method
    value = cursor.fetchall()
    # Tuple
    Pin_1 = value[0][0]
    Status_1 = value[0][1]
na    Pin_2 = value[1][0]
    Status_2 = value[1][1]
except:
    print ("Error: unable to fetch data")
finally:
    db.close()

def sendSignal() :
    for k in range(4):
        GPIO.output(pins[k], signal[step][k])

while True:
    db=MySQLdb.connect('localhost','root','1234567890','TestDB')
    # prepare a cursor object using cursor() method
    cursor =db.cursor()
    # execute SQL query using execute() method
    cursor.execute("select * from TestStatus WHERE Pin=1 or Pin=2")

    try:
        # Fetch a single row using fetchome method
        value = cursor.fetchall()
        # Tuple
        Pin_1 = value[0][0]
        Status_1 = value[0][1]
        Pin_2 = value[1][0]
        Status_2 = value[1][1]
    except:
        print ("Error: unable to fetch data")
    finally:
        db.close()


    if Status_1 == "On": 
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
            for i in range(512):
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
    
    
    
    if Status_2 == "ON":
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
            for i in range(512):
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
