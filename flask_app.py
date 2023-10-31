from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos local
conexion = mysql.connector.connect(user='root', password='password', host='localhost', database='Refrescos', port=3306)
cursor = conexion.cursor()

class SODA:
    def __init__(self, ID_SODA, NOMBRE, PRECIO, ENVASE, TAMANO, DESCUENTO, ID_MARCA):
        self.ID_SODA = ID_SODA
        self.NOMBRE = NOMBRE
        self.PRECIO = PRECIO
        self.ENVASE = ENVASE
        self.TAMANO = TAMANO
        self.DESCUENTO = DESCUENTO
        self.ID_MARCA = ID_MARCA

class MARCA:
    def __init__(self, ID_MARCA, NOMBRE):
        self.ID_MARCA = ID_MARCA
        self.NOMBRE = NOMBRE

@app.route('/sodas')
def sodas():
    try:
        cursor.execute("SELECT * FROM SODA")
        sodas_data = cursor.fetchall()
        sodas = [SODA(*row) for row in sodas_data]

        cursor.execute("SELECT * FROM MARCA")
        marcas_data = cursor.fetchall()
        marcas = [MARCA(*row) for row in marcas_data]

        return render_template('sodas.html', sodas=sodas, marcas=marcas)
    except mysql.connector.Error as err:
        # Manejar el error aquí, puedes imprimirlo o tomar otras medidas
        return f"Error en la consulta a la base de datos: {err}"

if __name__ == '__main__':
    app.run(debug=True)



