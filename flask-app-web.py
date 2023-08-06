from flask import Flask

app = Flask(__name__)

@app.route('/')
def careers_home():
    return "This is a careers page!"

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)