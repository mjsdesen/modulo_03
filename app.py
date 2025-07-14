from flask import Flask

# quando foi executado manualmente, vai ter essa formato __name__ == "__main__":
app = Flask(__name__)

#criação de rota
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/sobre')
def about():
    return "Esta é a sua página sobre."
# quando executado manualmente, vai ter esse formato __name__ == "__main__":
if __name__ == "__main__":
    # executa o servidor
    app.run(debug=True, host='localhost', port=5000)
