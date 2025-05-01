import mariadb


def conectar_y_consultar():
    try:
        conexion= mariadb.connect(
            host="localhost",
            database="almacen",
            user= "root",
            password="",
            port=3306 #puerto predeterminado para mariadb
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor Ounus")

        #crear un cursor y ejecutar la consulta
        cursor= conexion.cursor()
        consulta= "select * from usuarios"
        cursor.execute(consulta)

        #recurperar y mostrar resultados
        resultados=cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla: ")
        for fila in resultados:
            print(f"ID rol: {fila[0]}, Nombre completo: {fila[1]}, Nombre usuario:  {fila[2]}, correo {fila[3]}, contraseña: {fila[4]}")

        consulta2= "select * from roles"
        cursor.execute(consulta2)
        resultados2 = cursor.fetchall()
        print("Resultado", type(resultados2))
        print("Datos en la tabla: ")
        for fila in resultados2:
            print(f"Id: {fila[0]}, nombre de rol: {fila[1]}")
    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos {e}")

    finally:
            #cerrar la conexion y el cursor si etan abiertos
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion cerrada")




if __name__ == '__main__':
    conectar_y_consultar()