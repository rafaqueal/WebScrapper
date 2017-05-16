
import psycopg2
import datetime
##
##conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")



def insertAuditoria(date, errores, estado, registros):
    try:
        
        conn = psycopg2.connect(database="d2a95d9pumb48g", user="wykoxseytrhnfs",
                        password="aa3282757621c9f7d743b071dd82e43aba4ccf9a112d25cd819cea9db3eb0a82",
                        host="ec2-54-235-90-107.compute-1.amazonaws.com",
                        port="5432")
        cur = conn.cursor()
        print("INSERT INTO Auditoria (date, errores, estado, registros) \
        VALUES ('"+date+"', '"+errores+"', '"+estado+"', "+str(registros)+");")


        
        cur.execute("INSERT INTO auditoria (date, errores, estado, registros) \
        VALUES ('" +date+"', '"+errores+"', '"+estado+"', "+str(registros)+");");
        conn.commit()
        print("Records created successfully")
        conn.close()
        
    except:
        print("Ha ocurrido un problema con la insercion")

    
def insertCuponInfo(cupons):
    try:
        conn = psycopg2.connect(database="d2a95d9pumb48g", user="wykoxseytrhnfs", password="aa3282757621c9f7d743b071dd82e43aba4ccf9a112d25cd819cea9db3eb0a82", host="ec2-54-235-90-107.compute-1.amazonaws.com", port="5432")
        cur = conn.cursor()
        for j in range(len(cupons)):
            
            print("INSERT INTO cupon (title, subtitle, imgSrc, price, normalPrice, save, sold, exacHour, city, periodo, horary, direction, locationSrc, websiteSrc, facebookSrc) \
              VALUES ('"+cupons[j][0]+"','"+cupons[j][1]+"','"+cupons[j][2]+"','"+cupons[j][3]+"','"+cupons[j][4]+"','"+cupons[j][5]+"','"+cupons[j][6]+"','"+cupons[j][7]+"','"+
                        cupons[j][8]+"','"+cupons[j][9]+"','"+cupons[j][10]+"','"+cupons[j][11]+"','"+cupons[j][12]+"','"+cupons[j][13]+"','"+cupons[j][14]+"');")
            cur.execute("INSERT INTO cupon (title, subtitle, imgSrc, price, normalPrice, save, sold, exacHour, city, periodo, horary, direction, locationSrc, websiteSrc, facebookSrc) \
              VALUES ('"+cupons[j][0]+"','"+cupons[j][1]+"','"+cupons[j][2]+"','"+cupons[j][3]+"','"+cupons[j][4]+"','"+cupons[j][5]+"','"+cupons[j][6]+"','"+cupons[j][7]+"','"+
                        cupons[j][8]+"','"+cupons[j][9]+"','"+cupons[j][10]+"','"+cupons[j][11]+"','"+cupons[j][12]+"','"+cupons[j][13]+"','"+cupons[j][14]+"');")
            conn.commit()
        conn.close()
        
    except:
        print("Ha ocurrido un problema con la insercion de los cupones")
    
    


    

