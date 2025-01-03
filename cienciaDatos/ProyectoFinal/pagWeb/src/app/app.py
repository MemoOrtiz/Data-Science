import pickle
import os
from flask import Flask, render_template, request, jsonify


# Configurar Flask
app = Flask(__name__, 
            static_folder="../static", 
            template_folder="../templates")

# Obtener la ruta base de la carpeta actual
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cargar los modelos
ruta_clasificacion = os.path.join(BASE_DIR, 'model', 'modelo_de_clasificacion2.pkl')
ruta_regresion = os.path.join(BASE_DIR, 'model', 'modelo_de_regresion.pkl')

# Cargar los modelos
with open(ruta_clasificacion, 'rb') as file:
    modelo_clasificacion = pickle.load(file)
    print(type(modelo_clasificacion))
with open(ruta_regresion, 'rb') as file:
    modelo_regresion = pickle.load(file)
    

@app.route('/')
def index():
    return render_template('index.html')


# Ruta para la clasificación
@app.route('/clasificacion', methods=['POST'])
def clasificacion():
    data = request.get_json()  # Recibir datos en formato JSON
    input_data = data['features']  # Se espera un array de características
    
    print("Datos recibidos:", input_data)  # Debugging

    prediction = modelo_clasificacion.predict([input_data])
    return jsonify({'prediction': prediction.tolist()})

# Ruta para la regresión
@app.route('/regresion', methods=['POST'])
def regresion():
    data = request.get_json()
    input_data = data['features']
    print("Datos recibidos:", input_data)  # Debugging
    prediction = modelo_regresion.predict([input_data])
    return jsonify({'prediction': prediction.tolist()})

# Ejecución del servidor
if __name__ == '__main__':
    app.run(debug=True)