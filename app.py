from flask import Flask, render_template

PROJECTS = [
  {
    'id': 1,
    'title': 'Agente viajero con algoritmo de colonia de hormigas',
    'topic': 'Bioinspired algorithms',
    'programming_language': 'Python'
  },
  
  {
    'id': 2,
    'title': 'Geometric transformation of images',
    'topic': 'Image processing',
    'programming_language': 'Python'
  }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html', projects=PROJECTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)