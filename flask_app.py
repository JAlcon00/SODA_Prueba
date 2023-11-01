from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configura la conexión a la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/Refrescos'
db = SQLAlchemy(app)

class SODA(db.Model):
    ID_SODA = db.Column(db.Integer, primary_key=True)
    NOMBRE = db.Column(db.String(50), nullable=False)
    PRECIO = db.Column(db.Float, nullable=False)
    ENVASE = db.Column(db.String(50), nullable=False)
    TAMANO = db.Column(db.Float, nullable=False)
    DESCUENTO = db.Column(db.Float, nullable=False)
    ID_MARCA = db.Column(db.Integer, db.ForeignKey('marca.ID_MARCA'), nullable=False)

    marca = db.relationship('MARCA', primaryjoin='SODA.ID_MARCA == MARCA.ID_MARCA', back_populates='sodas')

class MARCA(db.Model):
    ID_MARCA = db.Column(db.Integer, primary_key=True)
    NOMBRE = db.Column(db.String(50), nullable=False)

    sodas = db.relationship('SODA', primaryjoin='SODA.ID_MARCA == MARCA.ID_MARCA', back_populates='marca')

@app.route('/')
def index():
    return "¡Bienvenido a la página de inicio!"

@app.route('/sodas')
def sodas():
    try:
        # Consulta los datos de sodas desde la base de datos local
        sodas = SODA.query.all()

        # Consulta las marcas desde la base de datos local
        marcas = MARCA.query.all()

        return render_template('sodas.html', sodas=sodas, marcas=marcas)
    except Exception as err:
        # Manejar el error aquí, puedes imprimirlo o tomar otras medidas
        return f"Error en la consulta a la base de datos: {err}"

if __name__ == '__main__':
    app.run(debug=True)
