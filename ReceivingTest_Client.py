import SocketToReceiverTest_Client as Sock
import time
import MySQLdb
import subprocess

subprocess.Popen(["python", "Clock_project4.py"])

db = MySQLdb.connect('localhost','root','1234567890','TestDB')

cursor = db.cursor()
sql = ""

try:
    while True:
        Sock.connection()
        time.sleep(5)
        r = str(Sock.sendingMsg()).split("'")
        print(r)
        rowCount = int(r[1])
        print(rowCount)
        
        if rowCount == "999.0":
            sql = "UPDATE TestStatus SET Status = 'On' WHERE Pin=1;"
            print(sql)
            cursorT.execute(sql)
            continue

        #sql = "UPDATE TestStatus SET Status = 'Off' WHERE Pin=1;"
        #cursor.execute(sql)

        for i in range(0,rowCount):
            receiving = str(Sock.sendingMsg())
            receiving = receiving[2:-1]
            print(receiving)

            li = receiving.split(" ")
            if li[3]=="False":
                sql = "UPDATE TestTable SET Location = 'Moving' WHERE Pin = '%s';" % (li[0])
            else:
                sql = "UPDATE TestTable SET Location = '%s' WHERE Pin = '%s';" % (li[0],int(li[0])-1)

            print(sql)
            cursor.execute(sql)

        print("While Finished")
        db.commit()

except:
    db.close()
