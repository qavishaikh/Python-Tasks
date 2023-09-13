from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! \n i am Qavi Shaikh'

if __name__ == '__main__':
    app.run()
