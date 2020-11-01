import mysql.connector

bd = mysql.connector.connect(
    user='sarahi',
    password='sayonarasaly4',
    database='cinemapp')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            "Id": row[0],
            "Correo": row[1],
            "Contraseña": row[2]
        }
        usuarios.append(usuario)
    
    return usuarios
