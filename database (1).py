import psycopg2

conn = psycopg2.connect(database="d2a95d9pumb48g", user="wykoxseytrhnfs",
                        password="aa3282757621c9f7d743b071dd82e43aba4ccf9a112d25cd819cea9db3eb0a82",
                        host="ec2-54-235-90-107.compute-1.amazonaws.com",
                        port="5432")
print ("Opened database successfully")

def createTables():
    cur = conn.cursor()

##    cur.execute('''CREATE TABLE scrapped
##       (ID SERIAL PRIMARY KEY     NOT NULL,
##       NAME           TEXT    NOT NULL);''')

    cur.execute('''CREATE TABLE Auditoria
       (ID SERIAL PRIMARY KEY     NOT NULL,
        Date TEXT NOT NULL,
        Errores TEXT NOT NULL,
        Estado TEXT NOT NULL,
        Registros INT NOT NULL);''')
    
    cur.execute('''CREATE TABLE Cupon
       (title TEXT NOT NULL,
        subtitle TEXT NOT NULL,
        imgSrc TEXT NOT NULL,
        price TEXT NOT NULL,
        normalPrice TEXT NOT NULL,
        save TEXT NOT NULL,
        sold TEXT NOT NULL,
        exacHour TEXT NOT NULL,
        city TEXT NOT NULL,
        periodo TEXT NOT NULL,
        horary TEXT NOT NULL,
        direction TEXT NOT NULL,
        locationSrc TEXT NOT NULL,
        websiteSrc TEXT NOT NULL,
        facebookSrc TEXT NOT NULL,
        PageID SERIAL PRIMARY KEY
        
        );''')
    
    print("Table created successfully")

    conn.commit()
    conn.close()

createTables()
