from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt = load('dt1.joblib')

# Generar el servidor (Back End)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
def formulario():
    return render_template('pagina1.html')

#Envio de datos a traves de JSON
@servidorWeb.route("/modelo", methods=["POST"])
def modeloPrediccion():
    # Procesar los datos de entrada
    contenido = request.json
    print(contenido)
    return jsonify({'resultado': 'ok'})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')