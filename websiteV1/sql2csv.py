import pymysql
import sys
import csv

def radiiNoiseGen():
    db = pymysql.connect("database-1.cluster-ro-cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()
    sql4 = ("UPDATE rehoboamSchema.rehoboamFull SET RADII = FLOOR(RAND()*(5000-100) + 100) #END")
    cursor.execute(sql4)
    db.commit()
    #sql2 = ("UPDATE rehoboamSchema.rehoboamFull SET RADII = RADII * 2 WHERE RADII < .00025")
    #cursor.execute(sql2)
    #db.commit()
    db.close()

def sql2csv():
    db = pymysql.connect("database-1.cluster-ro-cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
    cursor = db.cursor()

    sql1 = "SELECT indexKey, radii FROM rehoboamSchema.vw_rehoboam LIMIT 1000"
    cursor.execute(sql1)
    result=cursor.fetchall()

    c = csv.writer(open('rehoTestData.csv', 'w', newline=''))
    c.writerow(["indexKey", "Value"])
    for x in result:
        c.writerow(x) 

    db.close()

#radiiNoiseGen()
#sql2csv()

count = 0
while (count < 1000):
    radiiNoiseGen()
    sql2csv()
    count = count + 1
    print(count)
