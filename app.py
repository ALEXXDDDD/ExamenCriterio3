from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
  return '''<h1>Hola Alex</h1>
            <label>Contenidos</label>
            <button>INGRESAR</button>'''
if __name__=="__main__":
  app.run(debug=True)
