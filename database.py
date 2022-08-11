import sqlite3 
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('hoteldb.db')
        return con
    except Error:
        print(Error)

def sql_insert_reserva(num_reserva,check_in_date,check_out_date,costo_reserva,room_booking,user_booking):
    con = sql_connection()
    cur = con.cursor()
    cur.execute("insert into reserva(num_reserva,check_in_date,check_out_date,costo_reserva,room_booking,user_booking) values(?,?,?,?,?,?)",(num_reserva,check_in_date,check_out_date,costo_reserva,room_booking,user_booking))
    con.commit()
    con.close()