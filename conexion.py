import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        print('Se ha conectado a la db correctamente')
        return conexion
    except Error:
        print('Ha ocurrido un error')

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL)'''
    cursor.execute(sentencia_sql)
    conexion.commit()
    conexion.close

def insertar(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellidos) VALUES (?, ?)'
    cursor.execute(sentencia_sql, datos)
    conexion.commit()
    conexion.close

def insertar_varios(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellidos) VALUES (?, ?)'
    cursor.executemany(sentencia_sql, datos)
    conexion.commit()
    conexion.close

def consultar(conexion):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario'
    cursor.execute(sentencia_sql)
    datos = cursor.fetchall()
    conexion.close
    return datos

def consultar_por_id(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario WHERE id = ?'
    cursor.execute(sentencia_sql, (id, ))
    datos = cursor.fetchall()
    conexion.close
    return datos

def actualizar(conexion, id, nombre, apellidos):
    cursor = conexion.cursor()
    sentencia_sql = 'UPDATE usuario SET nombre = ?, apellidos = ? WHERE id = ?'
    cursor.execute(sentencia_sql, (nombre, apellidos, id))
    conexion.commit()
    conexion.close

def eliminar(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'DELETE FROM usuario WHERE id = ?'
    cursor.execute(sentencia_sql, (id, ))
    conexion.commit()
    conexion.close





conexion = conectar()
# crear_tabla(conexion)
# datos = ('Pablo', 'España')
# insertar(conexion, datos)
# datos = [('Pablo', 'España'), ('Jaime', 'Paz')]
# insertar_varios(conexion, datos)
# datos = consultar(conexion)
# for dato in datos:
#     print(dato[1] + ' ' + dato[2])
# datos = consultar_por_id(conexion, 4)
# if len(datos) > 0:
#     print(datos[0][1] + ' ' + datos[0][2])
# else:
#     print('No se encontro ese usuario')
# actualizar(conexion, 2, 'Cesar', 'Bravo')
eliminar(conexion, 2)