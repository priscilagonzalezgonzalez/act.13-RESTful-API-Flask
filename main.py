from flask import Flask, jsonify
from conexion import get_usuarios

app = Flask(__name__)

@app.route("/")
def hola():
    return "<b>Hola Mundo!<b>"

# @app.route("/usuarios/<string:nombre>")
# def usuarios(nombre):
#     return "Hola %s" % nombre

@app.route("/api/v1/usuarios")
def usuarios():
    usuarios_list = get_usuarios()

    #Convertir a formato JSON para que el navegador lo interprete
    return jsonify(usuarios_list)

app.run()