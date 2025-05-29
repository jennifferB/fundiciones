import mysql.connector
from mysql.connector import Error



def conectar_base_datos():
    try:
        # Establece la conexión
        conexion = mysql.connector.connect(
            host='localhost',       # Cambia por la dirección de tu servidor
            user='root',      # Reemplaza con tu usuario de MySQL
            password='',  # Reemplaza con tu contraseña de MySQL
            database='db_fundiciones'  # Reemplaza con el nombre de tu base de datos
        )
        
        if conexion.is_connected():
            print("Conexion exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

# Uso de la conexión
conexion = conectar_base_datos()
if conexion:
    # Cierra la conexión al finalizar
    conexion.close()