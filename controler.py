import sqlite3

def buscar_prestamos_vencidos():
    #llamar base de datos, return
    # conn = sqlite3.connect('libros.db')
    # cursor = conn.cursor()
    # filas = []
    # cursor.execute("SELECT * FROM prestamos")
    # prestamos = cursor.fetchall()
    # for prestamo in prestamos:
    #     id = prestamo[0]
    #     nombre = prestamo[1]
    #     apellido = prestamo[2]
    #     titulo_libro = prestamo[3]
    #     fecha_prestamo = prestamo[4]
    #     fecha_vencimiento = prestamo[5]
    #     filas.append((id, nombre, apellido, titulo_libro, fecha_prestamo, fecha_vencimiento))

    filas = [(1, 'Juan', 'Perez', 'El principito', '2021-10-01', '2021-10-15'),]
    #conn.close()
    return filas


