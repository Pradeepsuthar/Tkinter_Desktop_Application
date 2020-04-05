import pymysql as db

def getConnection(query, data):
    connection = db.connect(host='localhost',user='root',password='',db='Tally_ERP')

    cursor = connection.cursor()
    # cursor.execute("INSERT INTO Persons (Personid,PersonName) VALUES (2,'Pradeep Suthar');")

    count = cursor.execute(query, data)

    connection.commit()

    connection.close()

    return count

