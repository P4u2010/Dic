from flask import Flask
import random
import string

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas con adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
]

@app.route("/")
def hello_world():
    return '''
        <h1>Hello, World!</h1>
        <a href="/random_fact">¡Ver un dato aleatorio!</a><br>
        <a href="/generate_password">¡Generar una contraseña segura!</a>
    '''

@app.route("/random_fact")
def random_fact():
    fact = random.choice(facts_list)
    return f'<p>{fact}</p>'

@app.route("/generate_password")
def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return f'<p>Contraseña generada: <strong>{password}</strong></p>'

if __name__ == "__main__":
    app.run(debug=True)
