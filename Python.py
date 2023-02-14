from flask import Flask

app = Flask(__name__)

@app.route('/test/testo', methods=['GET'])
def hello_world():
    return 'Noyeu Janiversaire Leny!'

if __name__ == '__main__':
    app.run(debug=True,port=8089)
