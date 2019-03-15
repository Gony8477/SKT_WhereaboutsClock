# Raspberry pi Project in Software Engineering project
# Rpi.GPRO module and mysqldb use

import RPi.GPIO as GPIO
import time
import MySQLdb

# Open database Connection
db=MySQLdb.connect('localhost','root','1234567890','TestDB')
# prepare a cursor object using cursor() method
cursor =db.cursor()
# execute SQL query using execute() method
cursor.execute("select * from TestTable WHERE Pin=1 or Pin=2")

try:
    # Fetch a single row using fetchome method
    results = cursor.fetchall()
    for row in results:
            Pin_1 = row[0][0]
            Location_1 = row[0][1]
            Past_Location_1=row[0][2]
            Pin_2 = row[1][0]
            Location_2 = row[1][1]
            Past_Location_2=row[1][2]
except:
    print ("Error: unable to fetch data")

db.close()

# Clock signal
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

Pin_1 = row[0][0]
Location_1 = row[0][1]
Past_Location_1=row[0][2]
Pin_2 = row[1][0]
Location_2 = row[1][1]
Past_Location_2=row[1][2]

Pin_number_1= numbertest(Pin_1)
Pin_number_2= numbertest(Pin_2)
Now_Locate_1= test1(Location_1)
Now_Locate_2= test1(Location_2)
Past_Locate_1= test1(Past_Location_1)
Past_Locate_2= test1(Past_Location_2)

Answer_range_1= Angletest1(Past_Locate_1, Now_Locate_1)
Answer_range_2= Angletest1(Past_Locate_1, Now_Locate_1)
Pin1(Pin_number_1,Answer_range_1)
Pin2(Pin_number_2,Answer_range_2)


Real_Past_Locate_1= test2(Now_Locate_1)
Real_Past_Locate_2= test2(Now_Locate_2)


# input the Past_Location in DB
db=MySQLdb.connect('localhost','root','1234567890','TestDB')
cursor =db.cursor()
data1 = (Real_Past_Locate_1)
date2 = (Real_Past_Locate_2)
sql = "UPDATE TestTable SET Past_Location=%s WHERE Pin=%d;" % (data1, Pin_number_1)
sql = "UPDATE TestTable SET Past_Location=%s WHERE Pin=%d;" % (data2, Pin_number_2)
cursor.execute(sql,data)
db.commit()
db.close()


# Pin_number 1
def Pin1(Pin_number_1,Answer_range):
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
          for i in range(Answer_range_1):
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
def Pin2(Pin_number):
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
          for i in range(Answer_range_2):
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
