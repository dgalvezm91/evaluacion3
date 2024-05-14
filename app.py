from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_ejercicio1')
def form_ejercicio1():
    return render_template('form_ejercicio1.html')

@app.route('/form_ejercicio2')
def form_ejercicio2():
    return render_template('form_ejercicio2.html')

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = 'Aprobado'
    else:
        estado = 'Reprobado'

    return f'Promedio: {promedio}, Estado: {estado}'

@app.route('/nombre_mayor', methods=['POST'])
def nombre_mayor():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)

    return f'El nombre más largo es {nombre_mas_largo} con {len(nombre_mas_largo)} caracteres.'

if __name__ == '__main__':
    app.run(debug=True)
