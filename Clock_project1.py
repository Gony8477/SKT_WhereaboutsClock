#import Desktop.Software_Engineering.SocketToReceiverTest_Client as Sock
import RPi.GPIO as GPIO
import time
import MySQLdb

# Open database Connection
db=MySQLdb.connect('localhost','root','1234567890','TestDB')

# prepare a cursor object using cursor() method
cursor =db.cursor()

# execute SQL query using execute() method
cursor.execute("select * from TestTable")

try:
    # Fetch a single row using fetchome method
    results = cursor.fetchall()
    for row in results:
            Pin = row[0]
            Location = row[1]
            Past_Location=row[2]
except:
    print ("Error: unable to fetch data")

db.close()

def sendSignal() :
    for k in range(4):
        GPIO.output(pins[k], signal[step][k])

# Motor number
def numbertest(Pin):
    if Pin == 1:
          return 1
    elif Pin == 2:
          return 2

# Location Number
def test1(Location):
    if Location == 'School':
          return 1
    elif Location == 'Cafe':
          return 2
    elif Location == 'Hospital':
          return 3
    elif Location == 'home':
          return 4

# Location Number
def test2(Now_Locate):
    if Now_Locate == 1:
          return 'School'
    elif Now_Locate == 2:
          return 'Cafe'
    elif Now_Locate == 3:
          return 'Hospital'
    elif Now_Locate== 4:
          return 'Home'
"""
# Compare Location
def test2(Past_Locate,Now_Locate):
    if Past_Locate == Now_Locate:
        return 0
    else:
        return Now_Locate
"""
# Location compare and Angle
def Angletest1(Past_Locate, Now_Locate):
    if Past_Locate < Now_Locate:
        Answer= Now_Locate - Past_Locate
        if Answer ==1:
            return 128
        elif Answer ==2:
            return 256
        elif Answer ==3:
            return 384
    elif Past_Locate > Now_Locate:
        Answer= Past_Locate - Now_Locate
        if Answer== 1:
             return 384
        elif Answer==2:
             return 256
        elif Answer ==3:
             return 128
    elif Past_Locate == Now_Locate:
         return 0

# Main Function

Pin= row[0]
Location = row[1]
Past_Location= row[2]

Pin_number= numbertest(Pin)
Now_Locate= test1(Location)
Past_Locate= test1(Past_Location)

Answer_range= Angletest1(Past_Locate, Now_Locate)

Real_Past_Locate= test2(Now_Locate)


# input the Past_Location in DB
db=MySQLdb.connect('localhost','root','1234567890','TestDB')
cursor =db.cursor()
data = (Real_Past_Locate)
sql = "UPDATE TestTable SET Past_Location='babo' WHERE Pin=1;"
cursor.execute(sql,data)
db.commit()
db.close()


# Pin_number 1
if Pin_number==1:
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

# Pin_number 2
if Pin_number==2:
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
